

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('snippets/snip_man.html', views.man, name='man'),
    path('snippets/snip_about.html', views.about, name='about'),


    path('everything/', views.AllMaterialAvailable, name='AllMaterialAvailable'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]