from django.conf.urls import url
from mobapp import views
urlpatterns = [
    url(r'^home$',views.home,name = 'home'),
]    
