from django.shortcuts import render
from property.models import Property, Category
from agents.models import Agents
from django.db.models import Count

# Create your views here.

def home(request):
    template = 'home/home.html'
    category_list = Category.objects.annotate(property_count=Count('property')).values('category_name' , 'property_count' , 'image')
    print(category_list)
    property_list = Property.objects.all()
    agent_list = Agents.objects.all()
    context = {
        'category_lists': category_list,
        'property_lists': property_list,
        'agent_listing' : agent_list,
    }
    return render( request, template, context)