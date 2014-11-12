from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from Manager.models import Commercial
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Manager.forms import CommercialForm, RegistrationForm, CommercialUpdateForm
from django.core.urlresolvers import reverse
from exceptions import Exception
from django.contrib import messages
from django.views import generic

# Create your views here.

def ManagerDashboard(request):
    return render_to_response("Manager/html/Dashboard/index.html",context_instance=RequestContext(request))


def ManagerIndexCommercial(request):
    return render_to_response("Manager/html/Commercial/index.html",context_instance=RequestContext(request))


def ManagerSearchCommercial(request):
    all_ = Commercial.objects.all()
    paginator = Paginator(all_, 5)
    page = request.GET.get('page')
    
    try:
        liste = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        liste = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        liste = paginator.page(paginator.num_pages)
    
    return render_to_response("Manager/html/Commercial/liste.html", {'liste':liste},
                              context_instance=RequestContext(request))

class RegisterCommercial(generic.CreateView):
    form_class = RegistrationForm
    model = Commercial
    template_name = "Manager/html/Commercial/ajouter.html"
    #success_url = reverse(ManagerIndexCommercial);


    
class UpdateRegisteredCommercial(generic.UpdateView):
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





