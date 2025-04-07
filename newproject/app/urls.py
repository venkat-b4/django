from django.urls import path
from . import views
urlpatterns=[
    path('sample/',views.sample,name='sample'),
    path('students/',views.student,name='students'),
#    path('create_student/',views.create_student,name='create_student'),
    path('cards/',views.cards,name='cards'),
    path('employee/',views.employee, name='employee'),
    path('register/',views.user_register,name="user_register"),
   # path('user_detail/',views.user_detail,name="user_detail"),
]