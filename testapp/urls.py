from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from testapp import views


urlpatterns = [
    path('users/', views.datalist.as_view()),
    path('iou/', views.userupdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
