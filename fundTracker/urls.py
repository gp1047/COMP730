from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^deposit/', views.deposit, name="deposit"),
]
