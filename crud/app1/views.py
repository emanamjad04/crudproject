from django.shortcuts import render,redirect,HttpResponse
from .models import Student
# Create your views here.
def home(request):
    # return HttpResponse(
    #     '<h1>Hi home page</h2>'
    # )
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        city =  request.POST['city']
        contact = request.POST['contact']
        obj = Student(name=name, email=email,city=city,contact=contact)
        obj.save()
        return redirect('records')
    else:
        pass    
    return render(request, 'index.html')

def records(request):
    records=Student.objects.all()
    context ={
        'records':records
    }
    return render(request, 'records.html',context)

def delete(request,id):
    # print("ID: ",id)
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect('records')

def edit(request,id):
    data = Student.objects.get(id=id)
    context = {
        'data':data
        }
    return render(request, 'edit.html', context)

def update(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        city =  request.POST['city']
        contact = request.POST['contact']
        updatedrecord = Student(id=id,name=name,email=email,city=city,contact=contact)
        updatedrecord.save()
        print("name: ",id)
        return redirect('records')
    else:
        pass
    return render(request,'edit.html')    