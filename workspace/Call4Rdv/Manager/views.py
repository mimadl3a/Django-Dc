from django.shortcuts import render_to_response
from django.template.context import RequestContext
from Manager.models import Commercial
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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


def ManagerCreateCommercial(request):
    return ""


def ManagerUpdateCommercial(request):
    return ""


def ManagerDeleteCommercial(request):
    return ""