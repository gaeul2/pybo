from django.urls import path
from . import views

app_name = 'board'

urlpatterns =[
    path('', views.index, name='board'),
    path('<int:question_id>/', views.detail, name='question_detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
]