from django.db import models
from uuid import uuid4



def upload_image_book(instance, filename):
	return f"{instance.id_book}-{filename}"
	
class Books(models.Model):
	id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	status = models.IntegerField()
	create_at = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to=upload_image_book, blank=True, null=True)


