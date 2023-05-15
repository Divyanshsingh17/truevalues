from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect
from .models import Agents, Blog, About,Contact,Comment
from cars.models import NewCars,UsedCars
from . forms import CommentForm
from django.db.models import Q


# Create your views here.



def index(request):
    type = request.GET.get('type', "")
    search = request.GET.get('search', "")
    price = request.GET.get('price', "")
    body_type = request.GET.get('body_type', "")
   

    cars = NewCars.objects.all()
    usedcars = UsedCars.objects.all()
    # about = About.objects.get(id=1)
    
    if type == "New":
        if search:
            cars = NewCars.objects.filter(Q(car_name__icontains=search) | Q(body_type__icontains=search) | Q(color__icontains=search)) 
        
        if price:
            cars = cars.filter(exshowroom_price__lt = price)

        if body_type:
            cars = cars.filter(body_type = body_type)

        return render(request,'base/newcars.html', {"cars":cars,"search":search,"price":price,"Body Type": body_type})
    
    elif type == "Used":
        cars = usedcars
        print(cars)
        if search:
            cars = UsedCars.objects.filter(Q(usedcar_name__icontains=search)) 
        
        if price:
            cars = cars.filter(exshowroom_price__lt = price)

        if body_type:
            cars = cars.filter(body_type = body_type)
        print("-------##############--------")
        return render(request,'base/usedcars.html', {"cars":cars,"search":search,"price":price,"Body Type": body_type})
    else:
        print("---------------")
        return render(request,'base/index.html',{"cars":cars,"usedcars":usedcars, "about":about} )



def about(request):
    about = About.objects.get(id=1)
    return render(request,'base/about.html', {"about":about})



def agents(request):
    agents = Agents.objects.all()
    return render(request,'base/agents.html',{'agents':agents})



def blogs(request):
    blogs = Blog.objects.all()
    return render(request,'base/blogs.html',{"blogs":blogs})



def blogdetail(request,pk):
    blog = get_object_or_404(Blog,pk = pk)
    comments = Comment.objects.filter(blog_id = blog)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        print(request.user,request.user.id)
        parent_obj = None
        parent_id = request.POST.get('parent_id')
        if comment_form.is_valid:
            if parent_id =="":
                print("_________")
                new_comment = comment_form.save(commit=False)
                # assign ship to the comment
                new_comment.user = request.user
                new_comment.blog = blog
                # save
                new_comment.save()
            else:
                if parent_id:
                    parent_obj = Comment.objects.get(id=parent_id)
                    if parent_obj:
                    # create replay comment object
                        replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                        replay_comment.parent = parent_obj


        return HttpResponseRedirect('/blog/')
            # new_comment = comment_form.save(commit=False)
            # new_comment.user = request.user
            # new_comment.blog = blog
            # new_comment.save()
    else:
        comment_form=CommentForm()


    return render(request,'base/blogdetail.html',{"blog":blog,"comments":comments,"new_comment":new_comment,"comment_form":comment_form})




def contact(request): 
    if request.method == 'POST':
        print("________")
        full_name = request.POST['full_name']
        email = request.POST['email']
        contact = request.POST['contact']
        print("____________")
        message = request.POST['message']
        contact = Contact(full_name=full_name,email=email,contact=contact,message=message) 
        contact.save()
        context = {
            "success": True
        }
        return render(request,'base/contact.html',context)
    return render(request,'base/contact.html')


