from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class HomeView(View):

    template = 'home/index.html'
    context = {
        'title': 'Planificator',
        'title_page': "Home",
        'description_page': "Welcome on the home",
        # 'message': "Hello, world. You're at the home index.",
    }
    
    def get(self, request):
        context = self.context
        return render(
            request,
            self.template,
            context=context
        )
