from django.shortcuts import render

# Create your views here.

def forum(request):
    # trasactions = Transaction.objects.all()
    # return render(request, 'film_app/homepage.html', {'films': films})
    return render(request, 'forum_app/forum.html')