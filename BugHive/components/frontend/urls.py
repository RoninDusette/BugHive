from django.urls import path
from BugHive.components.frontend.views import MainTemplateView


urlpatterns = [
    path('home/', MainTemplateView.as_view(), name='main-view'),
]