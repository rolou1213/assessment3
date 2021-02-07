from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView 




# Create your views here.
def home(request):
   if request.method == 'POST':
    form = WidgetForm(request.POST)
   return render(request, 'home.html', {'form': form})

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'

class WidgetList(ListView):
  model = Widget


class WidgetDelete(DeleteView):
  model = Widget
  
