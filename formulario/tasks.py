from celery import shared_task
from django.core.mail import send_mail
from .models import Persona
@shared_task
def persona_created(persona_id):
    print("fadsfasdf")
    
    persona = Persona.objects.get(id=persona_id)
    subject = f'Nuevo registro # {persona.id}'
    message = f'Estimado {persona.nombre} {persona.apellido},\n\n' \
              f'Usted se ha registrado exitosamente en nuestro sitio'
    send_mail(subject,
                          message,
                          'test.django.pildoras@gmail.com',
                          [persona.email])
    return "Done"