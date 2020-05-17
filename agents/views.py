from django.shortcuts import render
from .models import Agents
# Create your views here.

def agents_list(request):
    agent_list = Agents.objects.all()
    template = 'agents/agents.html'
    context = {
        'agent_list' : agent_list
    }


    return render(request, template, context) 