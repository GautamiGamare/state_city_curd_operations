from django.shortcuts import render, redirect
from app1.forms import CityForm,StateForm,CuisineForm
from app1.models import CityModel,CuisineModel,StateModel

def state(req):
    return render(req,'state.html',{'form':StateForm(),'data':StateModel.objects.all()})

def save_state(req):
    ps = StateForm(req.POST,req.FILES)
    if ps.is_valid():
        ps.save()
        return redirect('state')
    else:
        print('Invalid')
        return render(req,'state.html',{'form':ps})

def update_state(req):
    num = req.GET.get('s1')
    St = StateModel.objects.get(id=num)
    return render(req,'update_state.html',{'data':St})

def updt_state(req):
    nm = req.POST.get('s1')
    ph = req.FILES.get('s2')
    num = req.POST.get('s3')
    StateModel.objects.filter(id=num).update(name=nm,photo=ph)
    return redirect('state')

def delete_state(req):
    num = req.GET.get('no')
    StateModel.objects.get(id=num).delete()
    return redirect('state')

def city(req):
    return render(req,'city.html',{'data':CityModel.objects.all(),
                                   'state':StateModel.objects.all()})

def save_city(req):
    cnm = req.POST.get('s1')
    cph = req.FILES.get('s2')
    snm = req.POST.get('s3')
    CityModel(name=cnm,photo=cph,city_state_id=snm).save()
    return redirect('city')

def update_city(req):
    num = req.GET.get('s1')
    St = CityModel.objects.get(id=num)
    return render(req, 'update_city.html', {'data': St})

def updt_city(req):
    nm = req.POST.get('s1')
    ph = req.FILES.get('s2')
    num = req.POST.get('s3')
    CityModel.objects.filter(id=num).update(name=nm, photo=ph)
    return redirect('city')

def delete_city(req):
    num = req.GET.get('no')
    CityModel.objects.get(id=num).delete()
    return redirect('city')

def add_cuisine(req):
    return render(req,'add_cuisine.html',{'form':CuisineForm(),'data':CuisineModel.objects.all()})

def save_cuisine(req):
    pf= CuisineForm(req.POST,req.FILES)
    if pf.is_valid():
        pf.save()
        return redirect('add_cuisine')
    else:
        print("error")
        return render(req,'add_cuisine.html',{'form':pf})
