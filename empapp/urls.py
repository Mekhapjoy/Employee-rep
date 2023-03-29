from django.urls import path

from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('updateemployee',views.updateemployee,name='update'),
    path('viewemployee',views.viewemployee,name='viewemployee'),
    path('deleteemployee <str:pk>',views.deleteemployee,name='delete1'),
    
]