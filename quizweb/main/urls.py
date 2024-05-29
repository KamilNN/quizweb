from django.urls import path
from .views import index, quiz_view, check, category_view, signup_view, login_view, view_results, WordList

urlpatterns = [
    path('', index, name='home'),
    path('categories/', category_view, name='category'),
    path('quiz/<int:category_id>', quiz_view, name='quiz'),
    path('check/<int:category_id>', check, name='check'),
    path('list/', WordList.as_view(), name='list'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('results/', view_results, name='results'),
]