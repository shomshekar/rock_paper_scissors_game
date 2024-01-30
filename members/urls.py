from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view-game/<slug:slug>', views.game_set, name='view-game'),
    path('result-page/', views.all_result, name='all-result'),
]
