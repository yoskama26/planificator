from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from organisation.models import Application,ApplicationMember,Collaborator


class CollaboratorView(View):

    template = 'team/collaborator.html'
    context = {
        'title': 'Planificator',
        'title_page': "Teams",
        'description_page': "Collaborator profil",
    }

    def get(self, request, collaborator_id=None):

        context = self.basecontext()

        if collaborator_id is not None:
            context.update({
                'collaborator_choosen': collaborator_id,
            })

        return render(
            request,
            self.template,
            context=context
        )

    def post(self, request):
        pass

    def basecontext(self, request=None):
        context = self.context.copy()
        data = {
            'collaborators': Collaborator.objects.all(),
        }
        context.update(data)
        if request is not None and 'collaborator_id' in request.POST:
            context.update({
                'collaborator_choosen': int(request.POST.get('collaborator_id')),
            })
        return context

