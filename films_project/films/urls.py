from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.film_list_view, name='all'),
    path('films/<int:pk>/detail/', views.film_detail_view, name='film_detail'),
    path('films/create/', views.film_create_view, name='film_create'),
    path('films/<int:pk>/update/', views.film_update_view, name='film_update'),
    path('films/<int:pk>/delete/', views.film_delete_view, name='film_delete'),
]
