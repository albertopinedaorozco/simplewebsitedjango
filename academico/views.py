from django.shortcuts import render
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model

from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView

from .models import Docente, Asignatura, Grupo

from django.urls import reverse_lazy

import json

class GrupoCreateView(CreateView):
    template_name ='academico/grupo_new.html'
    model = Grupo
    fields = '__all__'

class GrupoDetailView(DetailView):
    template_name = 'academico/grupo_detail.html'
    model = Grupo


class GrupoListView(ListView):
    template_name = 'academico/grupo_list.html'
    model = Grupo

class GruposDetailView(DetailView):
    template_name = 'academico/grupo_detail.html'
    model = Grupo

class AsignaturaDeleteView(DeleteView):
    template_name = 'academico/asignatura_delete.html'
    model = Asignatura
    success_url= reverse_lazy('asignatura_list')

class AsignaturaCreateView(CreateView):
    template_name = 'academico/asignatura_new.html'
    model = Asignatura
    fields = '__all__'
    

class AsignaturaDetailView(DetailView):
    template_name = 'academico/asignatura_detail.html'
    model = Asignatura


class AsignaturaListView(ListView):
    template_name = 'academico/asignatura_list.html'
    model = Asignatura


#usando render
def home(request):
    object_list = Docente.objects.all()
    return render(request,'academico/docentes_list.html', {'object_list': object_list })

#con platillas predefinidas
class DocenteListView(ListView):
    template_name = 'academico/docentes_list.html'
    model = Docente

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DocenteListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        
        empleados_descripcion  = Docente.objects.values('nombre')
        mydic = [x.get('nombre') for x in empleados_descripcion[0:5]]
        js_data_descripcion = json.dumps(mydic)
        
        #valores
        empleados_valores  = Docente.objects.values('edad')
        mydic = [x.get('edad') for x in empleados_valores[0:5]]
        js_data_valores = json.dumps(mydic)

        print(js_data_valores)

        context['empleados_descripcion'] = js_data_descripcion
        context['empleados_valores'] = js_data_valores
        return context

class DocenteDetailView(DetailView):
    template_name = 'academico/docente_detail.html'
    model = Docente

class DocenteCreateView(CreateView):
    template_name='academico/docentes_new.html'
    model = Docente
    fields = ['foto','nombre','apellidos','email']
    get_absolute_url  = reverse_lazy('docente_detail')

class DocenteUpdateView(UpdateView):
    template_name='academico/docente_edit.html'
    model = Docente
    fields = ['foto','nombre','apellidos','email']
    get_absolute_url  = reverse_lazy('docente_detail')


