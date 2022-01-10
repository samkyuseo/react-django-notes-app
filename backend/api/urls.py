from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('routes', views.get_routes, name='get_routes'),
    path('notes/add', views.add_note, name="add_note"),
    path('notes', views.get_notes, name="get_notes"),
    path('note/<str:pk>/update', views.update_note, name="update_note"),
    path('note/<str:pk>', views.get_note, name="get_note")
]
