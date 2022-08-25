from django.shortcuts import render, redirect, HttpResponse
from .models import Employees, Roles, Departments, Locations
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')





def all_employees_(request):
    emps = Employees.objects.all()
    data=list()
    mno=1
    for emp in emps:
        data.append([mno,emp]);
        mno+=1;
    context = {
        'datas': data,
    }
    return render(request, '_View_All_Employee_.html', context)





def add_employees_(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        location = int(request.POST['location'])
        role = int(request.POST['role'])
        new_emp = Employees(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, location_id = location, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('''<b> Employee added Successfully..... | 
            <a href='/'>HOME</a></b>''')
    role = Roles.objects.all()
    dept = Departments.objects.all()
    location = Locations.objects.all()
    context = {
        'roles' : role,
        'depts' : dept,
        'locations' : location,
    }
    return render(request, '_Add_Employee_.html', context)





def remove_employees_(request, emp_id = 0):
    if emp_id:
        emp_to_be_removed = Employees.objects.get(id=emp_id)
        emp_to_be_removed.delete()
        return HttpResponse('''<b> Employee Removed Successfully..... | 
            <a href='/'>HOME</a></b>''')
    emps = Employees.objects.all()
    context = {
        'emps': emps
    }
    return render(request, '_Remove_Employee_.html',context)





def filter_employees_(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        emps = Employees.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept_id = dept)
        if role:
            emps = emps.filter(role_id = role)
        if location:
            emps = emps.filter(location_id = location)
        data=list()
        mno=1
        for emp in emps:
            data.append([mno,emp]);
            mno+=1;
        context = {
            'datas': data,
            'pass': False,
        }
        return render(request, '_Filter_Employee_.html', context)

    role = Roles.objects.all()
    dept = Departments.objects.all()
    location = Locations.objects.all()
    print(location)
    context = {
        'roles' : role,
        'depts' : dept,
        'locations' : location,
        'pass': True,
    }
    return render(request, '_Filter_Employee_.html', context)





def update_employees_(request, emp_id = 0):

    if request.method == 'POST':
        hidden_id=request.POST['hidden_id'];
        lock=Employees.objects.get(pk=hidden_id)
        lock.first_name = request.POST['first_name']
        lock.last_name = request.POST['last_name']
        lock.salary = int(request.POST['salary'])
        lock.bonus = int(request.POST['bonus'])
        lock.phone = int(request.POST['phone'])
        lock.dept_id = int(request.POST['dept'])
        lock.role_id = int(request.POST['role'])
        lock.location_id = int(request.POST['location'])
        lock.hire_date = datetime.now()
        lock.save()
        return HttpResponse('''<b> Employee updated Successfully..... | 
            <a href='/'>HOME</a></b>''')

    # Code runs when we select any one person to update...
    if emp_id:
        emp_to_be_update = Employees.objects.get(id=emp_id)
        context = {
            'permit': 2,
            'emp': emp_to_be_update,
            'emps': Employees.objects.all(),
            'roles': Roles.objects.all(),
            'depts': Departments.objects.all(),
            'locations': Locations.objects.all(),
        }
        return render(request, '_Update_Employee_.html',context)

    # Code runs when we initially comes on update page...
    emps = Employees.objects.all()
    context = {
        'permit': 1,
        'emps': emps
    }
    return render(request, '_Update_Employee_.html',context)




