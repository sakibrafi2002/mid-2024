from django.views.generic import ListView
from .models import Project, Task

class ProjectTasksView(ListView):
    model = Task
    template_name = 'project_task.html'  # Update with your template path
    context_object_name = 'tasks'

    def get_queryset(self):
       # project_id = self.kwargs['project_id']
        return Task.objects.all().order_by(
            # Order by priority using custom ordering
            'priority'  # This orders by the string value of 'priority'
        )


