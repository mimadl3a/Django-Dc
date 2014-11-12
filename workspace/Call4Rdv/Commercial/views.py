from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from Commercial.models import Client, Commande, Calendrier
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Commercial.forms import ClientForm, LoginForm, get_form_cmd
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

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
    return render_to_response("Commercial/html/dashboard.html",
                              context_instance=RequestContext(request))



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


@login_required(login_url='/login/step1')
def ClientModifier(request, idClient):
    
    client = Client.objects.get(pk = idClient)
    formulaire = ClientForm(instance = client)
    
    if request.method == 'POST':
        
        if formulaire.is_valid:            
            f = ClientForm(request.POST, request.FILES, instance = client)
            f.save()
            messages.add_message(request, messages.INFO, 'Modification valide !')
            return redirect(reverse(ClientIndex))
        else:
            messages.add_message(request, messages.INFO, 'Modification invalide !')
            return redirect(reverse(ClientIndex))
        
    return render_to_response("Commercial/html/Client/modifier.html", 
                              {'formulaire':formulaire},
                              context_instance=RequestContext(request))
    
    














@login_required(login_url='/login/step1')
def CommandeIndex(request):
    return render_to_response("Commercial/html/Commande/index.html",context_instance=RequestContext(request))




def CommandeAjaxSearch(request):
    #clients = Client.objects.all()
    listeCommande = Commande.objects.all().filter(code__contains = request.POST['info'])
    paginator = Paginator(listeCommande, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    
    try:
        liste = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        liste = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        liste = paginator.page(paginator.num_pages)
    
    return render_to_response("Commercial/html/Commande/liste.html", {'liste':liste},
                              context_instance=RequestContext(request))


@login_required(login_url='/login/step1')
def CommandeModifier(request, idCommande):
    
    commande = Commande.objects.get(pk = idCommande)
    f = get_form_cmd([''])
    formulaire = f(instance = commande)
        
    if request.method == 'POST':
        if formulaire.is_valid:
            form = f(request.POST, request.FILES, instance = commande)
            form.save()
            messages.add_message(request, messages.INFO, 'Modification valide !')
            return redirect(reverse(CommandeIndex))
    return render_to_response("Commercial/html/Commande/modifier.html", 
                              {'formulaire':formulaire},
                              context_instance=RequestContext(request))


@login_required(login_url='/login/step1')
def CommandeCreate(request):
    
    #mform = ExampleForm()
        
    f = get_form_cmd(['dateReglement','preuveReglement'])
    formulaire = f()
    
    
    if request.method == 'POST':
        if formulaire.is_valid:
            form = f(request.POST, request.FILES)
            form.save()
            messages.add_message(request, messages.INFO, 'Commande cr&eacute;e !')
            return redirect(reverse(CommandeIndex))
    return render_to_response("Commercial/html/Commande/ajouter.html", 
                              {'formulaire':formulaire},
                              context_instance=RequestContext(request))
    
    






@login_required(login_url='/login/step1')
def CalendrierIndex(request):
    
    """send_mail('Subject here', 'Here is the message.', 'notifications@data-shore.com',
    ['rhdatacv@gmail.com'], fail_silently=False)"""
        
    liste_event = Calendrier.objects.all()
    data = """ """
    for event in liste_event:
        data += "{title: '"+event.title+"', start:'"+event.start+"', end:'"+event.end+"'},"
        
        
    return render_to_response("Commercial/html/Calendrier/index.html", 
                              {'data':data},
                              context_instance=RequestContext(request))


def CalendrierAjaxSave(request):
    
    titre = request.POST.get('titre')
    descr = request.POST.get('descr')
    date1 = request.POST.get('date1')
    date2 = request.POST.get('date2')
    
    c = Calendrier(title = titre, description = descr, start = date1, end = date2)
    c.save()
    
    return HttpResponse("ok")











