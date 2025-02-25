from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addnew', views.addnew, name='addnew'),
    path('edit/<int:id>/', views.edit, name='edit'),  # Add this line
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.destroy, name='destroy'),
]
