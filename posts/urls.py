from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('list/', views.post_list, name='list'),
    path('add/', views.add_post, name='add'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='detail'),
]