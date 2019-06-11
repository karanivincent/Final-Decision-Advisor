from django.urls import path
from assets_liabilities import views

app_name='assets'
urlpatterns = [
    path('assets/new/', views.CreateAssetsView.as_view(), name='assets_new'),
    path('assets/detail/<int:pk>/', views.AssetsDetailView.as_view(), name='assets_detail'),
    path('', views.AssetsListView.as_view(), name='assets_list'),
    path('assets/update/<int:pk>/', views.AssetsUpdateView.as_view(), name='assets_update'),
    path('assets/delete/<int:pk>/', views.AssetsDeleteView.as_view(), name='assets_delete'),
    
    #######################################################################################
    path('liabilities/new/', views.CreateLiabilitiesView.as_view(), name='liabilities_new'),
    path('liabilities/detail/<int:pk>/', views.LiabilitiesDetailView.as_view(), name='liabilities_detail'),
    path('liabilities/', views.LiabilitiesListView.as_view(), name='liabilities_list'),
    path('liabilities/update/<int:pk>/', views.LiabilitiesUpdateView.as_view(), name='liabilities_update'),
    path('liabilities/delete/<int:pk>/', views.LiabilitiesDeleteView.as_view(), name='liabilities_delete'),

]
