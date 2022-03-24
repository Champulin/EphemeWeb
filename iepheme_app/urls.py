from django.urls import path
from . import views
app_name = 'iepheme_app'
urlpatterns = [
    path('', views.VideoListView.as_view(), name='index'),
    path('category/<slug:slug>/', views.FilterListView.as_view(), name='category'),
    path('video/<int:pk>/', views.VideoDetailView.as_view(), name='video_player'),
    path('contact', views.ContactListView.as_view(), name='contact'),
]