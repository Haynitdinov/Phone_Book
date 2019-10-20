from django.urls import path, include
from phone_book_app import views

from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('new', views.new),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy, name='show'),
    path('search/', SearchResultsView.as_view(), name='show'),
]
