from django.db import models
from django.db.models.signals import pre_save

from apps.utils import unique_slug_gen


class ProjectType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank= True)
    description = models.TextField()
    summary = models.CharField(max_length=255, null=True, blank= True)
    img = models.URLField()
    back_img = models.URLField()
    project_type = models.ForeignKey(ProjectType,related_name='project_type' ,on_delete=models.CASCADE)
    started = models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.title
        

def pre_save_reciver(sender, instance , *args, **kwargs):
    if not instance.slug:
        instance.slug =unique_slug_gen(instance)

pre_save.connect(pre_save_reciver, sender =Project)
