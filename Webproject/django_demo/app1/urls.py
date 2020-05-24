from django.urls import path, re_path
from app1 import views as app1_views

urlpatterns = [
    re_path(r'^articles/(?P<year>[0-9]{4})/$', app1_views.article),
    # path('get_name', app1_views.get_name),
    path('get_name', app1_views.PersonFormView.as_view()),
    path('person_detail/<int:pk>', app1_views.person_detail),
]