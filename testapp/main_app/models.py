from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Videos(models.Model):
	title = models.CharField(max_length = 250)
	description = models.TextField(null = True, blank = True)
	file = models.FileField(upload_to = 'videos', validators=[FileExtensionValidator(['mp4', 'flv', '3gp', 'avi', 'wmv', 'mov' , 'm3u8' ])])

	def __str__(self):
		return self.title


