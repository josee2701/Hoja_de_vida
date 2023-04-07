from django.db import models

# Create your models here.
from django.db import models

# Se crea modelos los cuales estan divididos en 7 clases para poder realizar la creación de una hoja de vida

class Profile(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.name + self.last_name

class Contact(models.Model):
    
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=200)
    redes = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Professional_profile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description
    
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
class Education(models.Model):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Interest(models.Model):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title