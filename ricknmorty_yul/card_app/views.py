from django.shortcuts import render

# Create your views here.

def home_page(request):
    # trasactions = Transaction.objects.all()
    # return render(request, 'film_app/homepage.html', {'films': films})
    return render(request, 'card_app/homepage.html')
