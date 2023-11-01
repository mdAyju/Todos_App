from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from app. models import DataModel
from app.forms import DataForm
from django.contrib import messages
from django.http import JsonResponse


def show(request):
    all=DataModel.objects.all()
    return render(request,'all.html',locals())

class Register(View):
    def get(self,request):
        form= DataForm()
        return render (request,'enter.html',locals())
    
    def post(self,request):
        form= DataForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            fin=DataModel(name=name,locality=locality,mobile=mobile,state=state,zipcode=zipcode).save()
            messages.success(request,'Details Saved Succesfully')
        else:
            messages.warning(request,'Invalid data')
        return render(request,'enter.html',locals())
        
def remove(request):
    if request.method=='GET':
        prod_id= request.GET.get('prod_id')
        rem = DataModel.objects.get(id=prod_id)
        print(rem)
        rem.delete()
        return redirect('show')
    
class Edit(View):
    def get(self,request,pk):
        data = DataModel.objects.get(id=pk)
        form=DataForm(instance=data)
        return render(request,'edit.html',locals())
    
    def post(self,request,pk):
        form = DataForm(request.POST)
        data= DataModel.objects.get(id=pk)
        if form.is_valid():
            data.name=form.cleaned_data['name']
            data.locality=form.cleaned_data['locality']
            data.mobile=form.cleaned_data['mobile']
            data.state=form.cleaned_data['state']
            data.zipcode=form.cleaned_data['zipcode']
            data.save()
            messages.success(request,'Details are edited')
        else:
            messages.warning(request,'not edited')
        return redirect('show')


