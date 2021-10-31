from django.urls import path

from Bookapp import views

app_name= 'Bookapp'

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('library/<int:library_id>/',views.view,name="view"),
    path('update/<int:id>/',views.update, name="update"),
    path('delete/<int:id>/',views.delete, name="delete"),
    path('add/', views.add_library, name="add_library"),


]