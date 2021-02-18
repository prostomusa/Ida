from django import forms
from .models import Picture
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from resizeimage import resizeimage

class ImageForm(forms.Form):
	url_image = forms.URLField(help_text="Ссылка", required=False)
	image = forms.ImageField(help_text="Файл", required=False)

class PicForm(forms.ModelForm):
	class Meta:
		model = Picture
		fields = ['height', 'width']

		labels = {
		    'height': 'высота',
		    'width': 'ширина',
		}