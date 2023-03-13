import random

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import *
from .models import *
from .workers_data import add_to_database


def index(request):
    # add_to_database()

    # uncomment only if you need to add new employees to the database, use fixtures instead

    allworkers = Workers.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allworkers, 5)

    try:
        workers = paginator.page(page)
    except PageNotAnInteger:
        workers = paginator.page(1)
    except EmptyPage:
        workers = paginator.page(paginator.num_pages)

    return render(request, 'app_tree/index.html', context={
        'workers': workers
    })


def workers_list_view(request):
    form = WorkersListForm()
    if 'choice' in request.GET:
        choice = request.GET['choice']
        workers = Workers.objects.order_by(choice)[:10]
    else:
        workers = Workers.objects.all()[:10]
    return render(request, 'app_tree/workers_info.html', context={
        'workers': workers, 'form': form,
    })


class WorkerUpdate(UpdateView):
    template_name = 'app_tree/worker_update.html'
    form_class = WorkerUpdateForm
    model = Workers
    success_url = reverse_lazy('workers')
