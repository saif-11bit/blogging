from django.urls import path
from .views import IndexView, BlogView, ContactView, BlogDetail

app_name = 'blogApp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blogdetail/<slug>/', BlogDetail.as_view(), name='blogdetail')
]
