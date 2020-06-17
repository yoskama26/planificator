from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/userprofile/login/'), name='dispatch')#permet de cacher la view si l'utilisateur n'est pas connecté et le redirige vers le login(décorateur)
class TeamView(View):

    template = 'team/team.html'
    context = {
        'title': 'Planificator',
        'title_page': "Teams",
        'description_page': "Welcome on the teams home",
    }
    
    def get(self, request):

        context = self.basecontext()

        return render(
            request,
            self.template,
            context=context
        )

    def post(self, request):
        pass

    def basecontext(self, request=None):
        context = self.context.copy()
        return context

