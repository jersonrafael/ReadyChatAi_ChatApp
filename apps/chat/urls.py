from django.urls import path
from .views import *
urlpatterns = [
    path('messages/', chat_home_view, name="chat"),
    path('message/<int:id>/', chat_message_view, name="message"),
    path('my/message/<int:pk>/', chat_my_message_view, name="message"),
    path('message/send/', send_message_view, name="sed_message"),
    path('login/', chat_login_view, name="login"),
    path('start/', chat_singup_view, name="create_account"),
    path('logout/', chat_logout_view, name="logout"),


]