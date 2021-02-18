from django.shortcuts import render, redirect
from django.views.generic import View
from .form import *
from .models import *
import urllib.request
from django.contrib import messages
from PIL import Image, UnidentifiedImageError
from .ratio import ratio
# Create your views here.

def main_page(request):
	pictures = Picture.objects.all()
	return render(request, 'pictures/index.html', context={'pics': pictures})


class Add_Pic(View):

	def get(self, request):
		form = ImageForm()
		return render(request, 'pictures/add_pic.html', context={'form': form})

	def post(self, request):
		bound_form = ImageForm(request.POST, request.FILES)
		if bound_form.is_valid():
			if bound_form['image'].value() and bound_form['url_image'].value():
				messages.info(request, 'Нельзя заполнять два поля')
			elif bound_form['image'].value():
				im = Image.open(bound_form['image'].value())
				width1, height1 = im.size[0], im.size[1]
				temp = Picture.objects.create(image = bound_form['image'].value(), height = height1, width = width1)
				temp.save()
				return redirect('edit_page', id_image=temp.id)
			elif bound_form['url_image'].value():
				temp = Picture.objects.create(image = 'temp.jpg')
				temporary = "pics/{}.jpg".format(temp.id)
				place = "media/pics/{}.jpg".format(temp.id)
				resource = urllib.request.urlopen(bound_form['url_image'].value())
				out = open(place, 'wb')
				out.write(resource.read())
				out.close()
				try:
					im = Image.open(place)
					temp.height = im.size[1]
					temp.width = im.size[0]
					temp.image = temporary
					temp.save(update_fields=["image", "height", "width", "base_height", "base_width"])
					return redirect('edit_page', id_image=temp.id)
				except UnidentifiedImageError:
					temp.delete()
					messages.info(request, 'Неправильный формат картинки')
			else:
				messages.info(request, 'Заполните одно поле')
		return render(request, 'pictures/add_pic.html', context={'form': bound_form})


class Edit_Pic(View):

	def get(self, request, id_image):
		picture = Picture.objects.get(id=id_image)
		form = PicForm(instance=picture)
		ratio_width, ratio_height = ratio(picture)
		context = {'form': form, 'pic': picture, 'w': ratio_width, 'h': ratio_height} 
		return render(request, 'pictures/edit_pic.html', context)


	def post(self, request, id_image):
		picture = Picture.objects.get(id=id_image)
		bound_form = PicForm(request.POST, instance=picture)
		if bound_form.is_valid():
			bound_form.save()
			return redirect('edit_page', id_image=picture.id)
		return render(request, 'pictures/edit_pic.html', context={'form': bound_form, 'picture': picture})

