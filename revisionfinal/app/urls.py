from django.conf.urls import url
from app import views

app_name="app"

urlpatterns=[
    url(r'^registrations/$',views.registration,name="registration"),
    url(r'^user_login/',views.user_login,name="user_login")
]
