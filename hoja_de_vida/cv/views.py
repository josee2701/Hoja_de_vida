import json

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    TemplateView)
from .models import Profile, Education,Experience,Contact,Skill,Interest,Professional_profile


from django.db.models import Q

# Create your views here.

class TemplatePerfil(TemplateView):


    template_name = 'perfil.html'

    def get_queryset(self):
        return Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = Profile.objects.first()  # Obtener el primer perfil del conjunto
        contact = Contact.objects.first()
        descrision = Professional_profile.objects.first()
        educacion = Education.objects.all()
        habilidades= Skill.objects.all()
        esperiencia = Experience.objects.all()
        context.update({"perfil": perfil,"contact":contact, "descrision":descrision, "educacion":educacion,"habilidades":habilidades,"esperiencia":esperiencia})
        return context