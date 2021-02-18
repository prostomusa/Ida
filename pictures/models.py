from django.db import models


class Picture(models.Model):
	height = models.IntegerField(null=True)
	width = models.IntegerField(null=True)
	base_width = models.IntegerField(blank=True, null=True)
	base_height = models.IntegerField(blank=True, null=True)
	image = models.ImageField(upload_to='pics/')

	def save(self, *args, **kwargs):
		if not self.base_width:
			self.base_width = self.width
			self.base_height = self.height
		super().save(*args, **kwargs)

	def __str__(self):
		return (str(self.id) + ".jpg")
# Create your models here