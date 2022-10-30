from django.urls import path

from final_exam.web import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('catalogue/', views.show_catalogue, name='show catalogue'),
    path('car/create/', views.create_car, name='create car'),
    path('car/<int:pk>/details/', views.show_car, name='show car'),
    path('car/<int:pk>/edit/', views.edit_car, name='edit car'),
    path('car/<int:pk>/delete/', views.delete_car, name='delete car'),

    path('profile/create/', views.create_profile, name='create profile'),
    path('profile/details/', views.show_profile, name='show profile'),
    path('profile/edit/', views.edit_profile, name='edit profile'),
    path('profile/delete/', views.delete_profile, name='delete profile'),
]
