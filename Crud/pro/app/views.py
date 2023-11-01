from django.shortcuts import render,HttpResponse,redirect
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import MobileDrf
from app.models import MobileModel

# Create your views here.

@api_view(['GET'])
def index(request):
    getting =MobileModel.objects.all()
    Api=MobileDrf(getting,many=True)
    return Response(Api.data)

@api_view(['get'])
def onlyOne(request,pk):
    obj = MobileModel.objects.get(id=pk)
    resp=MobileDrf(obj,many=False)
    return Response(resp.data)

@api_view(['POST'])
def post(request):
    res=MobileDrf(data=request.data)
    if res.is_valid():
        res.save()
    return Response(res.data)

@api_view(['POST'])
def edit(request,pk):
    editing= MobileModel.objects.get(id=pk)
    res=MobileDrf(instance=editing,data=request.data)
    if res.is_valid():
        res.save()
    return Response(res.data)

@api_view(['DELETE'])
def remove(request,pk):
    rem= MobileModel.objects.get(id=pk)
    rem.delete()
    return Response(rem.data)

def main(request):
    res=MobileModel.objects.all()
    return render(request,'index.html',locals())

def add(request):
    import pdb;pdb.set_trace()
    if request.method=='POST':
        name=request.POST.get('name')
        price= request.POST.get('price')
        ram =request.POST.get('ram')
        storage=request.POST.get('storage')
        FormRes =MobileModel(mobiles=name,price=price,ram=ram,storage=storage)
        FormRes.save()
    return render(request,'index.html',locals())
