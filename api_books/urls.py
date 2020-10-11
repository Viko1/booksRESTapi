from django.urls import path
from .views import GenericAPIView, BooksAPIView, BookDetails


urlpatterns = [
    path('books/', BooksAPIView.as_view()),
    path('books/<int:id>/', BookDetails.as_view()),
    path('books/genricandfilter/', GenericAPIView.as_view())
]
