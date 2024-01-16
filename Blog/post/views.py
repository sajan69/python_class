from django.shortcuts import render

from .models import BlogPost, Category
from .forms import Category , PostForm
def index(request):
    posts = BlogPost.objects.all().filter(is_active=True)
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories
    }
    
    return render(request, 'post/index.html', context)

def post_details(request, id):
    post = BlogPost.objects.get(id=id) 
    context = {
        'post': post,
    }
    return render(request, 'post-details.html', context)

def create_post(request):
    form = createPostForm()
    if request.method == "POST":
        title = request.POST.get('title')
        if title == "":
            messages.error(request, "Title field is required.")
            return HttpResponseRedirect('/create-post')
        category = Category.objects.get(id=request.POST.get('category'))   
        content = request.POST.get('content')
        if content == "":
            messages.error(request, "Content field is required.")
            return HttpResponseRedirect('/create-post')
        image = request.FILES.get('image')
        if image == "":
            messages.error(request, "Image field is required.")
            return HttpResponseRedirect('/create-post')
        is_active = request.POST.get('is_active')
        is_featured = request.POST.get('is_featured')

        if is_active == "on":
            is_active = True
        else:
            is_active = False

        if is_featured == "on":
            is_featured = True
        else:
            is_featured = False

        post = Blog_Post.objects.create(
            title = title,
            category = category,
            author = request.user,
            content = content,
            image = image,
            is_active = is_active,
            is_featured = is_featured,
        )
        post.save()
        messages.success(request, f"{title} is Created Successfully.")
        return HttpResponseRedirect('/create-post')

    context = {
        'form':form,
        'categories':categories,
    }
    return render(request, 'post/create-post.html', context)
