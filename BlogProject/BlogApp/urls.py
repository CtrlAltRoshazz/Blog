from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view , name= "home"),
    path("addblog/" , views.addblog_view , name= "addblog"),
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("updateblog/<int:id>/", views.updateblog_view, name="updateblog"),
    path("deleteblog/<int:id>/", views.deleteblog_view, name="deleteblog"),
]
