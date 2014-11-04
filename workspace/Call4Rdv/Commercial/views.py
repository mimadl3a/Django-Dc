from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from Commercial.models import Client
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Commercial.forms import ClientForm, LoginForm
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def Mlogin(request):
    #INIT FORM TO TEMPLATE
    form = LoginForm()
    
    #IF DATA IS SENT
    if request.method == 'POST':
        #PASS DATA FORM LOGIN FORM TO HANDLE IT
        form = LoginForm(data = request.POST)
        if form.is_valid():
            login1 = request.POST['username']
            pass1 = request.POST['password']
            
            user = authenticate(username=login1, password=pass1)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse(ClientIndex))
            else:
                messages.add_message(request, messages.INFO, "Utilisateur introuvable")
                return redirect(reverse(Mlogin))
        else:
            messages.add_message(request, messages.INFO, "Formulaire invalide")
            
    
    return render_to_response("Commercial/html/Login/index.html",{'formulaire':form},
                              context_instance=RequestContext(request))


def Mlogout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "A bientot !")
    return redirect(reverse(Mlogin))
    










def dashboard(request):
    return render_to_response("Commercial/html/dashboard.html")



def liste(request):
    return HttpResponse("hello")
    

@login_required(login_url='/login/step1')
def ClientIndex(request):
    return render_to_response("Commercial/html/Client/index.html",
                              context_instance=RequestContext(request))



def ClientAjaxSearch(request):
    #clients = Client.objects.all()
    listeClient = Client.objects.all().filter(nom__contains = request.POST['info'])
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
    
    return render_to_response("Commercial/html/Client/liste.html", {'liste':clients},
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








