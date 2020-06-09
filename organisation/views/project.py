from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from organisation.models import Project


class ProjectView(View):

    template = 'project/baseproject.html'
    context = {
        'title': 'Planificator',
        'title_page': "Projects",
        'description_page': "Welcome on the projects home",
        # 'message': "Hello, world. You're at the home index.",
    }

    def get(self, request):

        context = self.context
        projects = Project.objects.all()
        context.update({
            'projects': projects,
        })

        return render(
            request,
            self.template,
            context=context
        )

