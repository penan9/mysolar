import os
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import models
from django.dispatch import receiver


def UploadedConfigPath(instance, filename):
       return os.path.join('images', str(instance.directory), filename)
#       return os.path.join(settings.MEDIA_ROOT, 'images', str(instance.directory), filename)


class Image(models.Model):
    name = models.CharField(max_length=50, default='')
    directory = models.CharField(max_length=50, default='home')
    file= models.FileField(upload_to=UploadedConfigPath, blank=True, verbose_name="", default='')

    def __str__(self):
        return str(self.file)

    def snippet(self):
        return self.directory


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_imagefile_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    print ("post delete ...")
    print (sender)
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    print ("pre save image ...")
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).file
        new_file = instance.file
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)

    except ValueError:
        print ("Exception: ValueError")
        return False

    except sender.DoesNotExist:
        print ("Exception: DoesNotExist")
        print (sender)
        return False


class Home(models.Model):
    name = models.CharField(max_length=50, default='')
    file= models.FileField(upload_to='video/home', blank=True, verbose_name="", default='')

    def __str__(self):
        return str(self.file)

    def snippet(self):
        return self.file


@receiver(models.signals.post_delete, sender=Home)
def auto_delete_file_on_delete(sender, instance, **kwargs):

    print ("post delete home ...")
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Home)
def auto_delete_file_on_change(sender, instance, **kwargs):
    print ("pre save home ...")
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).file
        new_file = instance.file
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)

    except ValueError:
        print ("Exception: ValueError")
        return False

    except sender.DoesNotExist:
        print ("Exception: DoesNotExist")
        print (sender)
        return False
