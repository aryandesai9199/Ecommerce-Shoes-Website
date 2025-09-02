from django.shortcuts import redirect, render

# Create your views here.

def admin_page(request):
    return render(request, "admin_page.html")

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('/adm/admin_page')
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials"})
    return render(request, "admin_login.html")