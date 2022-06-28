from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path('about', views.about, name="about"),
               path('teams', views.teamss, name="teams"),
               path('schedule', views.schedules, name="schedule"),
               path('teammembers', views.teamsmembers, name="teammmembers")]
#urlpatterns = [path("teammembers/", views.players, name="players")]
