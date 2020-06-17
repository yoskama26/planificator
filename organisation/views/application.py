from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from organisation.models import Application,ApplicationMember
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/userprofile/login/'), name='dispatch')#permet de cacher la view si l'utilisateur n'est pas connecté et le redirige vers le login (décorateur)
class ApplicationView(View):

    template = 'team/application.html'
    context = {
        'title': 'Planificator',
        'title_page': "Teams",
        'description_page': "Application team",
        # 'message': "Hello, world. You're at the home index.",
    }

    def get(self, request, application_id=None):

        context = self.basecontext()
        if application_id is not None:
            context.update({
                'application_choosen': application_id,
                'members': ApplicationMember.objects.filter(application__id=application_id)
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
            'applications': Application.objects.all(),
        }
        context.update(data)
        if request is not None and 'application_id' in request.POST:
            context.update({
                'application_choosen': int(request.POST.get('application_id')),
            })
        return context

