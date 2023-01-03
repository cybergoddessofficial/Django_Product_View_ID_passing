
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index,name="Index"),
    path('shop/<int:product_id>',views.shop,name="shop")
]
