from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm = request.POST.get('password2')
        print(password)
        print(confirm)
        if password!=confirm:
            return render(request, 'register.html', {
                "error":"Password didn't match try again"
            })
        
    return render(request, 'register.html')

def logout(request):
    return render(request, 'logout.html')