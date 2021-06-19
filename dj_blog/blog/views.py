from django.shortcuts import render
 
post = [
     {
         'author':'Emmanuel Kpogo',
         'title':'Why we got to live',
         'content':'First post content',
         'Date':'24th June 2004'
     },
     {
         'author':'Joshua Kpogo',
         'title':'We are been perfected',
         'content':'Second post content',
         'Date':'27th April 2004'
     },
     {
         'author':'Stephen Kpogo',
         'title':'Great things take time',
         'content':'Third post content',
         'Date':'24th March 2014'
     }
 ]


def home(request):
    context = {
    'posts': post
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})

# Create your views here.
