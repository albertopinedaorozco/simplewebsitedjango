from django.urls import path
from .views import home,DocenteListView,DocenteCreateView,DocenteDetailView, DocenteUpdateView, AsignaturaListView,AsignaturaDetailView,AsignaturaCreateView,AsignaturaDeleteView,GrupoListView,GrupoDetailView,GrupoCreateView

urlpatterns = [
    path('', DocenteListView.as_view(), name='docentes_list'),
    
    #path('', home, name='docentes_list'),
    path('docente/new/', DocenteCreateView.as_view(), name='docente_new'),
    path('docente/<int:pk>/', DocenteDetailView.as_view(), name='docente_detail'),
    path('docente/<int:pk>/edit/', DocenteUpdateView.as_view(), name='docente_edit'),
    path('asignatura/', AsignaturaListView.as_view(), name='asignatura_list'),
    path('asignatura/<int:pk>/edit/', AsignaturaDetailView.as_view(), name='asignatura_detail'),
    path('asignatura/new/', AsignaturaCreateView.as_view(), name='asignatura_new'),
    path('asignatura/<int:pk>/delete/', AsignaturaDeleteView.as_view(), name='asignatura_delete'),
    path('grupo/', GrupoListView.as_view(), name='grupo_list'),
    path('grupo/<int:pk>', GrupoDetailView.as_view(), name='grupo_detail'),
    path('grupo/new/', GrupoCreateView.as_view(), name='grupo_new'),
]