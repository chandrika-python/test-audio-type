from django.urls import path
from audio import views

urlpatterns = [
    path('create/',views.create,name="create"),
    path('get/<str:audioFileType>/<int:audioFileID>/',views.get,name="detail"),
    path('get/<str:audioFileType>/',views.get,name="details"),
    path('delete/<str:audioFileType>/<int:audioFileID>/',views.delete,name="delete"),
    path('update/<str:audioFileType>/<int:audioFileID>/',views.update,name="update")
]
