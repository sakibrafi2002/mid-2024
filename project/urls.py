from .views import ProjectTasksView
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('tasks/', ProjectTasksView.as_view()),
    path('test/',TemplateView.as_view(template_name='project_task.html')),
]