from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/edit', views.FinchEdit.as_view(), name='finch_edit'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
]

# For edit an create, Django uses the same form.html file. For items rendered on that page that are unique to create or edit, you can use conditional visibility (if, else)