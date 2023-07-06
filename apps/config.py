from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from .home.models import Estudiante, Profesor

class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
    label = 'apps'

    def ready(self):
        from django.contrib.auth.models import User

        @receiver(post_save, sender=User)
        def create_user_profile(sender, instance, created, **kwargs):
            if created:
                # Obtener el valor del parámetro enviado desde el formulario
                user_type = instance.profile_type  # Asumiendo que el campo se llama 'profile_type'

                if user_type == 'estudiante':
                    Estudiante.objects.create(user=instance)

                elif user_type == 'profesor':
                    Profesor.objects.create(user=instance)
