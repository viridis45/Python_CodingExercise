from django.urls import path, include
from . import views




app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),    # ex: /polls/
#     path('<int:question_id>/', views.detail, name='detail'), # ex: /polls/5/
#     path('<int:question_id>/results/', views.results, name='results'), # ex: /polls/5/results/
#     path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/
# ]

# using the general view form
# https://docs.djangoproject.com/en/3.2/intro/tutorial04/
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('tester-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]