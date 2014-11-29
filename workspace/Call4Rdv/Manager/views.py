from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from Manager.models import Commercial
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Manager.forms import RegistrationForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def custom_404(request):
    return render_to_response('Manager/html/templates/404.html', RequestContext(request))

def custom_500(request):
    return render_to_response('Manager/html/templates/500.html', RequestContext(request))


    


def Managerlogin(request):
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
                    return redirect(reverse(ManagerDashboard))
            else:
                messages.add_message(request, messages.INFO, "Utilisateur introuvable")
                return redirect(reverse(Managerlogin))
        else:
            messages.add_message(request, messages.INFO, "Formulaire invalide")
            
    
    return render_to_response("Manager/html/Login/index.html",{'formulaire':form},
                              context_instance=RequestContext(request))


def Managerlogout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "A bientot !")
    return redirect(reverse(Managerlogin))
    






@login_required(login_url='Managerlogin/step1')
def ManagerDashboard(request):
    return render_to_response("Manager/html/Dashboard/index.html",context_instance=RequestContext(request))


def ManagerIndexCommercial(request):
    page = 1
    try:
        if request.method == 'GET':   
            page = request.GET['page']
    except:
        page = 1
    
    
    
    return render_to_response("Manager/html/Commercial/index.html",
                              {'page':int(page)},
                              context_instance=RequestContext(request)
                              )


def ManagerSearchCommercial(request):
    all_ = Commercial.objects.all()
    paginator = Paginator(all_, 5)
    page = request.REQUEST['page']
    
    
    try:
        liste = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        liste = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        liste = paginator.page(paginator.num_pages)
    
    return render_to_response("Manager/html/Commercial/liste.html", {'liste':liste, 'page':int(page)},
                              context_instance=RequestContext(request))

class RegisterCommercial(CreateView):
    #recuperer objet
    mon_objet = Commercial.objects.get(pk=11)
    
    form_class = RegistrationForm
    model = Commercial
    #initier le nom par valeur objet
    initial = {'nom':mon_objet.nom}
    template_name = "Manager/html/Commercial/ajouter.html"
    #success_url = reverse(ManagerIndexCommercial);


    
class UpdateRegisteredCommercial(UpdateView):
    form_class = RegistrationForm
    model = Commercial
    template_name = "Manager/html/Commercial/modifier.html"
    #success_url = reverse(ManagerIndexCommercial);


    
    
"""

def ManagerCreateCommercial(request):
    formulaire = CommercialForm()
    if request.method == 'POST':
        if formulaire.is_valid:
            form = CommercialForm(request.POST)
            form.save()
            messages.add_message(request, messages.INFO, 'Commercial cr&eacute;e !')
            return redirect(reverse('indexCommercial'))
        
    return render_to_response("Manager/html/Commercial/ajouter.html", {'formulaire':formulaire},
                              context_instance=RequestContext(request))




def ManagerUpdateCommercial(request, idCommercial):
    commercial = Commercial.objects.get(pk = idCommercial)
    formulaire = CommercialUpdateForm(instance = commercial)
    
    if request.method == 'POST':
        if formulaire.is_valid:
            form = CommercialUpdateForm(request.POST, instance = commercial)
            try:
                form.save()
                messages.add_message(request, messages.INFO, "Sauvegarde ok !")
                return redirect(reverse('indexCommercial'))
            except Exception as e:
                messages.add_message(request, messages.INFO, e.message)
                #return HttpResponse(e.message)
                #return redirect(reverse('indexCommercial'))
            
    
    return render_to_response("Manager/html/Commercial/modifier.html",{'formulaire':formulaire},
                              context_instance=RequestContext(request))
"""

def ManagerDeleteCommercial(request):
    return ""





