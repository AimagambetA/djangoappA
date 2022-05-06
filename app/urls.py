from django.urls import path
from . import views
from .views import *

urlspatterns ={
    path('send/',send_message)
    path('post/<int:post_id>',views.show_post,name='post')
}