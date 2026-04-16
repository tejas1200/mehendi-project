from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),  # /admin/
    
    path('login/', views.admin_login),  # /admin/login/
    path('logout/', views.admin_logout),
    path('add-image/', views.add_image),
    path('bookings/', views.booking_list),

    path('delete-image/<int:id>/', views.delete_image),
    path('edit-image/<int:id>/', views.edit_image),
    
    path('categories/', views.categories),
    path('delete-category/<int:id>/', views.delete_category),

    path('gallery/', views.gallery),
]