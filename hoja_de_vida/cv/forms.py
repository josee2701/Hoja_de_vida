""" Modelos asociados al módulo de reporte en tiempo real.

Este módulo crea los modelos de la base de datos utilizados para crear vehículos, dispositivos, y
almacenar los datos de las tramas. También crea una tabla de relación entre el tipo de dispositivo,
el número de evento y el evento que reporte el dispositivo (elemento IO).

Para una mayor referencia sobre la creación de modelos en Django, consulte
https://docs.djangoproject.com/en/4.1/topics/db/models/
"""

from django import forms
from .models import Profile, Education,Experience,Contact,Skill,Interest,Professional_profile
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class ProfileFroms(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["name", "last_name", "career", "photo",]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "career": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "photo": forms.FileInput(
                attrs={
                    "class": "form-control",
                },
            ),
        }
    
class ContactFroms(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["phone", "email", "city", "redes",]
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "redes": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
        }

class Professional_profileFroms(forms.ModelForm):
    
    class Meta:
        model = Professional_profile
        fields = ["profile", "description",]
        widgets = {
            "profile": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
        }
        
class SkillFroms(forms.ModelForm):
    
    class Meta:
        model = Skill
        fields = ["profile", "title", "description",]
        widgets = {
            "profile": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
        }


class ExperienceFroms(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ["profile", "job_title", "company", "start_date", "end_date", "description",]
        widgets = {
            "profile": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "job_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "company": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
        }


class EducationFroms(forms.ModelForm):
    
    
    class Meta:
        model = Education
        fields = ["profile", "degree", "institution", "start_date", "end_date", "description",]
        widgets = {
            "profile": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "degree": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "institution": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
        }

class InterestFroms(forms.ModelForm):
    
    class Meta:
        model = Interest
        fields = ["profile", "title", "description",]
        widgets = {
            "profile": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
        }
    
# Path: hoja_de_vida\cv\forms.py