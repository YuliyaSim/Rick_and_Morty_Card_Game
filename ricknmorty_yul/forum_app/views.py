from django.shortcuts import render

# Create your views here.

def forum(request):
    # thread = Thread.objects.all()
    # return render(request, 'forum_app/forum.html', {'comment': comment})
    return render(request, 'forum_app/forum.html')