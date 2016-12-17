from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Show, ShowForm
#from .forms import ShowForm

# Create your views here.

def index(request):
    show_list = Show.objects.order_by('run_date')
    context = {'show_list': show_list}
    return render(request, 'shows/index.html', context)

def edit(request, show_id):
    show = get_object_or_404(Show, pk=show_id)  
    form = ShowForm(instance=show)
    return render(request, 'shows/edit.html', {'show': show, 'form': form})
    
def add(request):
    form = ShowForm()
    return render(request, 'shows/add.html', {'form': form})

def update(request, show_id):
    show = get_object_or_404(Show, pk=show_id)  
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('shows:index')
        else:
            return render(request, 'shows/edit.html', {'show': show, 'form': form})

def create(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shows:index')
        else:
            return render(request, 'shows/add.html', {'form': form})

def delete(request, show_id):
    show = get_object_or_404(Show, pk=show_id)  
    show.delete()
    return redirect('shows:index')