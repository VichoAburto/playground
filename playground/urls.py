from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.character_list, name='character_list'),
    path('character/', views.character_list, name='character_list'),
    path('character/<str:id_character>/', views.character_detail, name='character_detail'),
    path('character/<str:id_character>/?<str:message>', views.character_detail, name='character_detail_mes'),
    path('equipement/', views.equipement_list, name='equipement_list'),
    path('equipement/<str:pk>/', views.equipement_detail, name='equipement_detail'),
]
