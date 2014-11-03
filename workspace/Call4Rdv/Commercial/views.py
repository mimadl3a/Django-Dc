from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from Commercial.models import Client
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Commercial.forms import ClientForm
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.



def dashboard(request):
    return render_to_response("Commercial/html/dashboard.html")



def liste(request):
    return HttpResponse("hello")
    


def ClientIndex(request):
    
    #clients = Client.objects.all()
    listeClient = Client.objects.all()
    paginator = Paginator(listeClient, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clients = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clients = paginator.page(paginator.num_pages)
    return render_to_response("Commercial/html/Client/index.html", {'liste':clients},
                              context_instance=RequestContext(request))



def ClientAjaxSearch(request):
    listeClient = Client.objects.all()
    
    return render_to_response("Commercial/html/Client/index.html", {'liste':listeClient},
                              context_instance=RequestContext(request))



def ClientModifier(request, idClient):
    
    client = Client.objects.get(pk = idClient)
    formulaire = ClientForm(instance = client)
    
    if request.method == 'POST':
        if formulaire.is_valid:
            f = ClientForm(request.POST, request.FILES, instance = client)
            f.save()
            messages.add_message(request, messages.INFO, 'Modification valide !')
            return redirect(reverse(ClientIndex))
    return render_to_response("Commercial/html/Client/modifier.html", 
                              {'formulaire':formulaire},
                              context_instance=RequestContext(request))








