from django.shortcuts import render
from .forms import PersonaForm
from .tasks import persona_created

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save()
            persona_created.delay(persona.id)
    else:
        form = PersonaForm()
    return render(request, 'form.html', {'form': form})