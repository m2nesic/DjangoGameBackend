from django.urls import path
from django.views.generic import TemplateView

app_name = 'review'
urlpatterns = [
    path('',TemplateView.as_view(template_name = "review/index.html")),
    
]
