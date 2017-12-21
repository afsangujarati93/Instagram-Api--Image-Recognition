from django.shortcuts import render
from django.http import HttpResponse
from InstaIR.Log_Handler import Log_Handler as lh
from django import forms
from InstaIR.IR_Router import InstaMain as im


class NameForm(forms.Form):
    user_name = forms.CharField(label = '', max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control input-lg',
            'style': 'margin-top: 20px',
            'placeholder':'Username'
        }))

logger = lh.log_initializer()
def index(request):
	try:
		#load the UI for user
		#ask user to enter a username for performing sentiment analysis on its tweets
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = NameForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				user_name = form.cleaned_data['user_name']
				recent_media_list = im.insta_get_images(user_name)				
				str_recent_media = '~'.join(recent_media_list)				
				#return the received response from prediction back to the UI classying among positives and negatives
				return render(request, 'insta_image.html', {					
					'recent_media':str_recent_media,					
					})

			# if a GET (or any other method) we'll create a blank form
		else:
			form = NameForm()
			return render(request, 'index.html', {'form': form})

	except Exception as Ex:
		logger.error("Exception occurred in the index method| Exception:" + str(Ex))
		return render(request, 'index.html')
	# return HttpResponse("Exception occurred in the index method| Exception:" + str(Ex))
	# Create your views here.

def object_recognition(request):
	METHOD_NAME = 'object_recognition'
	try:
		image_name = request.GET['image_name']
		print('image_name:' + str(image_name))
		object_file_details = im.insta_recog_object(image_name)
		image_name = object_file_details.image_name
		object_details_list = object_file_details.obj_name_prob
		object_name_list = []
		object_prob_list = []
		for object_details in object_details_list:
			print("Object Name:" + str(object_details.object_name) +"\t :" +  str(object_details.object_prob))
			object_name_list.append(object_details.object_name)
			object_prob_list.append(str(object_details.object_prob))        
		print("\n\n") 
		str_object_names = "~".join(object_name_list)
		str_object_probs = "~".join(object_prob_list)
		return render(request, 'final_result.html',{
			'image_name' : image_name,
			'object_name_list' : str_object_names,
			'object_prob_list' : str_object_probs,
			})
		# return HttpResponse("File Name:" + image_name + "     object name and prob:" + str_object_names + "  |prob: " + str_object_probs)
	except Exception as Ex:
		logger.error("Exception occurred in the "+object_recognition+" method| Exception:" + str(Ex))
		return render(request, 'index.html')
	else:
		pass
	finally:
		pass
