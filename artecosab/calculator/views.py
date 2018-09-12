''' calculator views '''

from django.views import generic
from .models import Server

class IndexView(generic.ListView):
    ''' home page showing all servers in a list '''

    template_name = "index.html"
    context_object_name = "all_servers"

    def get_queryset(self):
        return Server.objects.all()

class ServerView(generic.DetailView):
    ''' a server's details page showing cameras '''

    template_name = "server.html"
    model = Server
