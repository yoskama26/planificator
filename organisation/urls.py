from django.urls import path,re_path
from django.conf.urls import url
from .views import project,team,application,collaborator


urlpatterns = [
    path('project/', project.ProjectView.as_view(), name='project'),
    path('project/<int:project_id>/', project.ProjectView.as_view(), name='project'),
    path('team/', team.TeamView.as_view(), name='team'),
    path('collaborator/', collaborator.CollaboratorView.as_view(), name='collaborator'),
    re_path(r'^collaborator/(?P<collaborator_id>\d+)/$', collaborator.CollaboratorView.as_view(), name='collaborator'),
    # path('collaborator/<int:collaborator_id>/', collaborator.CollaboratorView.as_view(), name='collaborator'),
    path('application/', application.ApplicationView.as_view(), name='application'),
    re_path(r'^application/(?P<application_id>\d+)/$', application.ApplicationView.as_view(), name='application'),
    # path('application/<int:application_id>/', application.ApplicationView.as_view(), name='application'),
]
