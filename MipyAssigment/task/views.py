from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def firstApp(request):
    uf=UserForm(request.POST)
    if request.method=="POST":
        if uf.is_valid():
            name=uf.cleaned_data['name']
            email=uf.cleaned_data['email']
            phno=uf.cleaned_data['phoneno']
            age=uf.cleaned_data['age']
            dob=uf.cleaned_data['dob']
            uf.name=name
            uf.email=email
            uf.phoneno=phno
            uf.age=age
            uf.dob=dob
            uf.save()
            messages.success(request,"User Details saved successfully")
            return redirect('secondapp')

        else:
            return render(request,"index.html",{'uf':uf})

    return render(request,"index.html",{'uf':uf})


def secondApp(request):
    if request.method =='POST':
        name=request.POST.get('n1')
        try:
            Ud=User.objects.filter(name__icontains=name)
            #print(Ud)
            return render(request,"userDet.html",{'ud':Ud})
        except User.DoesNotExist:
            return render(request,"userDet.html",{"error":"Details Doesnt Exists...!"})
    else:
        return render(request,"userDet.html")