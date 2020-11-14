from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Products.as_view()),
    path('product/', views.SingleProduct.as_view()),
    path('product/<int:id>', views.SingleProduct.as_view()),
    path('tags/', views.Tags.as_view()),
    path('tag/', views.SingleTag.as_view()),
    path('export-products/', views.ExportToCSV.as_view()),
    path('import-products/', views.ImportProduct.as_view()),
]
