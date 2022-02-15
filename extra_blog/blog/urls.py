from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.PostView.as_view(), name ='index'),
    path('post/<int:pk>/',views.PostDetailView.as_view()),
    path('comments/<int:pk>/',views.AddComment.as_view(),name="comments")
]