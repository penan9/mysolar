import os
from django.db import models
from django.utils import timezone
from procedures.models import Procedure
from django.dispatch import receiver


class Product(models.Model):
	name = models.CharField(max_length=255)
	youtubeID = models.CharField(max_length=255, null=True, blank=True, default="")
	code = models.ForeignKey(Procedure, default='1', verbose_name='Procedure', null=True, blank=True, on_delete=models.SET_NULL)
	code2 = models.CharField(max_length=10, default="")
	price = models.FloatField()
	price2 = models.FloatField(default='0.0')
	stock = models.IntegerField()
	unit = models.CharField(max_length=100, default='brls')
	doc = models.IntegerField(default=0)
	button_name = models.CharField(max_length=100, default='procedure')
	photo = models.ImageField(upload_to='images/products', blank=True, default='')
	date = models.DateTimeField(auto_now_add=True)
	#date = models.DateTimeField(default=timezone.now)


	def __str__(self):
            id = format(self.id, '05d')
            return str(id) + " - " + str(self.name)


class Offer(models.Model):
	code = models.CharField(max_length=10)
	description = models.CharField(max_length=255)
	discount = models.FloatField()
	mode = models.CharField(max_length=255)


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    print ("post delete ... ")
    print (sender)
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    print ("pre save ... ")
    print (sender)
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).photo
        new_file = instance.photo
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except ValueError:
        print ("Exception: ValueError")
        return False
    except sender.DoesNotExist:
        return False


def UploadedConfigPath(instance, filename):
      id = str(instance.product)[0:5]
      print ("At UploadedConfigPath ID: " + id)
      imageFileName = os.path.join('gallery', id, str(instance.directory), filename)
      print ("Original imagefilename: "+ imageFileName)
      dir = os.path.join('gallery')
      prefix, extension = os.path.splitext(imageFileName)
      print ("prefix: "+ prefix + " ext: " + extension)
      instance.thumbnail = imageFileName
      if ((extension == ".doc") or (extension == ".docx")):
          instance.thumbnail = dir + "/thumbnail/word.png"
      elif (extension == ".pdf"):
          instance.thumbnail = dir + "/thumbnail/pdf.png"
      print ("thumbnail: "+ instance.thumbnail)
      return imageFileName


class ProductDetail(models.Model):
	title = models.CharField(max_length=255)
	productid = models.CharField(max_length=50)
	product = models.ForeignKey(Product, default='1', verbose_name='Product', null=True, blank=True, on_delete=models.SET_NULL)
	desc = models.CharField(max_length=255, default="")
	directory = models.CharField(max_length=50, blank=True, default="")
	photo = models.FileField(upload_to=UploadedConfigPath, blank=True, default='')
	thumbnail = models.CharField(max_length=255, blank=True, default='')
	date = models.DateTimeField(auto_now_add=True)


def update_product_doc(pid):
    print ("update product doc, id: "+pid+".")
    try:
        product_details = ProductDetail.objects.filter(productid=pid)
        print ("product details:")
        print (product_details)
        product = Product.objects.get(id=int(pid))
        print ("product:")
        print (product.name)
        product.doc = product_details.count()
        product.save()
        print ("after: " + str(product.doc))
    except AttributeError:
        print ("Exception: AttributeError")
        return False
    except ValueError:
        print ("Exception: ValueError")
        return False
    except Product.DoesNotExist:
        print ("Exception: product DoesNotExist")
        return False
    except ProductDetail.DoesNotExist:
        print ("Exception: ProductDetail DoesNotExist")
        return False


@receiver(models.signals.post_delete, sender=ProductDetail)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    print ("post delete ... ")
    print (sender)
    if instance.photo:
        print ("in instance.photo ... ")
        print (instance.photo)
        if os.path.isfile(instance.photo.path):
            print ("in instance.photo.path ... ")
            print (instance.photo.path)
            os.remove(instance.photo.path)
    pid = str(instance.product)[0:5]
    update_product_doc(pid)


@receiver(models.signals.pre_save, sender=ProductDetail)
def auto_presave_file_on_change(sender, instance, **kwargs):
    print ("pre save ... ")
    pid = str(instance.product)[0:5]
    print ("pid: " + pid)
    instance.productid = pid


@receiver(models.signals.post_save, sender=ProductDetail)
def auto_delete_file_on_change(sender, instance, **kwargs):
    print ("post save ... ")
    print (instance.title)
    print ("pid: " + instance.productid)
    if not instance.pk:
        print (instance.pk)
        return False
    update_product_doc(instance.productid)
    try:
        old_file = sender.objects.get(pk=instance.pk).photo
        print ("instance.pk: "+str(instance.pk))
        new_file = instance.photo
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except ValueError:
        print ("Exception: ValueError")
        return False
