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
    username = request.session['username']
    return render(request,'cards.html',context={'username':username})

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')  
        print("jack")         
        if password == confirm_password:
            if user_data.objects.filter(username=username).exists():
                return HttpResponse("username exits")
            elif user_data.objects.filter(email=email).exists():
                return HttpResponse("email exits")
            else:
                print("jack")
                user = user_data.objects.create(
                    username = username,
                    password = password,
                    email = email
                )
                user.save()
                return redirect('cards')
        else:
            print("jack")
            return HttpResponse("password exits")
        # return redirect('employee')
    return render(request, 'register.html')     

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')

        user_det = user_data.objects.get(username = username)
        if user_det:
            
            if user_det.password== password:
                request.session['username']=username
                return redirect('cards')
            else:
                return HttpResponse("wrong password")
        else:
            return HttpResponse(f"{username}")
    return render(request,'loginPage.html')
            
