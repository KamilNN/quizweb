from django.urls import path
from .views import index, quiz_view, check, category_view, WordList

urlpatterns = [
    path('', index, name='home'),
    path('categories/', category_view, name='category'),
    path('quiz/<int:category_id>', quiz_view, name='quiz'),
    path('check/<int:category_id>', check, name='check'),
    path('list/', WordList.as_view(), name='list'),
]