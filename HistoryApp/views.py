from django.shortcuts import render
from HistoryApp.models import*
from django.http import HttpResponse
from HistoryApp.forms import*
# Create your views here.
def tema(self):

    tema = Temas(nombre='Imperio Egipcio', categoria='Historia Antigua')
    tema.save()

    documentDeTexto= f'-----> nombre: {tema.nombre}, categoria: {tema.categoria}'

    return HttpResponse(documentDeTexto)


def home(request):
    return render(request,'home.html')

def usuarios(request):
    return render(request,'usuarios.html')

def admins(request):
    return render(request, 'admins.html')

def membresia(request):
    return render(request, 'membresia.html')

def temas(request):
    if request.method == 'POST':
        miFormulario = TemaFormulario(request.POST) # Este lugar donde llega la informacion de html 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            tema = Temas(nombre=informacion['tema'], categoria=informacion['categoria'])
            tema.save()
            return render(request, 'home.html')
    else:
        miFormulario = TemaFormulario()
    return render(request, 'temas.html', {'miFormulario': miFormulario})

def adminFormulario(request):
    if request.method == 'POST':
        miFormulario = AdminFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            admin = Admin(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'],cargo=informacion['cargo'])
            
            admin.save()

            return render(request, 'home.html')
        
    else:
        miFormulario = AdminFormulario()

    return render(request, 'adminFormulario.html',{'miFormulario':miFormulario})

def usuarios(request):
    if request.method == 'POST':
        miFormulario = UsuarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario = Usuarios(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'],edad=informacion['edad'])
            
            usuario.save()

            return render(request, 'home.html')
        
    else:
        miFormulario = UsuarioFormulario()

    return render(request, 'usuarioFormulario.html',{'miFormulario':miFormulario})

def busquedaTema(request):
    return render(request, 'busquedaTema.html')

def busqueda(request):
    if request.GET['categoria']:

        # respuesta = f"Estoy buscando el tema: {request.GET['tema']}"
        categoria = request.GET['categoria']
        tema = Temas.objects.filter(categoria__icontains=categoria)
        return render(request, 'home.html',  {'tema':tema,'categoria': categoria})
    
    else:
        respuesta = 'No enviaste datos'

    return render(request, 'home.html', {'respuesta': respuesta})
