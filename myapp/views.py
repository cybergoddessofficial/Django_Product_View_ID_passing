from django.shortcuts import render
from myapp.models import shopDB
# Create your views here.


def Index(request):
	data=shopDB.objects.all()
	return render(request,"index.html",{'data':data})
	
def shop(request,product_id):
	product=shopDB.objects.get(id=product_id)
	return render(request,"details.html",{'product':product})
