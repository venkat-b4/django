from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student,Employee,user_data     

def sample(request):
    return render(request,'sample.html')    

def employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        email = request.POST['email']
        gender = request.POST['gender']
        department = request.POST['department']
        print(first_name,last_name,age,email,gender,department)
        Employee.objects.create(
            first_name = first_name,
            last_name = last_name,
            age = age,
            email = email,
            gender = gender,
            department = department
        )
        return redirect('employee')
    return render(request,'employee.html')
    # return render(request,'sample.html')
# def students(request):
#     return render(request)
    # data = student.object.filter(id=1)
    # update = student.object.get(id=1)
    # update.name = 'jack'
    # update.save()
    # print(data)
    # l= []
    # return HttpResponse('students')
def cards(request):
    return render(request,'cards.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')           
        if 1 == 1:
            if user_data.objects.filter(username=username).exists():
                return HttpResponse("username exits")
            if user_data.objects.filter(email=email).exists():
                return HttpResponse("email exits")
            else:
                user = user_data.objects.create(
                    username = username,
                    password = password,
                    email = email
                )
                user.save()
                return redirect('cards')
        # return redirect('employee')
    return render(request, 'register.html')     
       
