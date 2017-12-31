import requests
from xml.etree import ElementTree
import json
from InstaIR.Log_Handler import Log_Handler as lh
import urllib.request
import os

logger = lh.log_initializer()

class InstaApi:
	cofig_file = open("InstaIR/config.json").read()
	global config_json
	config_json = json.loads(cofig_file)

	def save_image(image_url, image_predic_folder):
		METHOD_NAME = 'save_image'
		try:			
			image_name = image_url.split('/')[-1]
			image_predic_path = image_predic_folder + r'/' + image_name
			logger.info('Saving Image %s', image_predic_path)			
			urllib.request.urlretrieve(image_url, image_predic_path)  			
			return image_name     
		except Exception as Ex:
			logger.error("Exception occurred in the "+ METHOD_NAME +" method| Exception:" + str(Ex))

	def insta_getuserid(user_name):
		METHOD_NAME = "insta_getuserid"
		try:
			access_token = config_json['InstagramApi']['AccessToken']
			logger.debug('Inside: ' + METHOD_NAME)
			#urls can go to config file if required
			str_url = "https://api.instagram.com/v1/users/search?q={0}&access_token={1}"
			api_response = InstaApi.insta_getcall(str_url = str_url, a = user_name, b = access_token)
			#assuming that the user will always provide an extact username, 
			#for future purpose you may give the output result and let the user select one and accordingly get the userid
			user_id = api_response['data'][0]['id']
			return user_id

		except Exception as Ex: 
			logger.error("Exception Occurred in:" + METHOD_NAME + "|Exception:" + str(Ex))


	def insta_getrecentmedia(user_id):
		METHOD_NAME = "insta_getrecentmedia"
		try:
			access_token = config_json['InstagramApi']['AccessToken']
			logger.debug('Inside: ' + METHOD_NAME)
			str_url = "https://api.instagram.com/v1/users/{0}/media/recent/?access_token={1}"

			api_response = InstaApi.insta_getcall(str_url = str_url, a = user_id, b = access_token)
			image_urls_list = []

			#checking if directory has files and if yes, deleting all the files before saving new ones
			dir_path = os.path.dirname(os.path.realpath(__file__))
			image_predic_folder = dir_path + r'/static/Prediction Images'
			logger.info("Directory name:" + str(dir_path))			
			if os.listdir(image_predic_folder):
				print("Directory has files")
				for image_file in os.listdir(image_predic_folder):
					image_file_path = os.path.join(image_predic_folder, image_file)										
					os.remove(image_file_path)
				logger.info("Deleting file completed from directory:" + image_predic_folder)
			else:
				print("No files in directory")

			for data in api_response['data']:
				image_url = data['images']['standard_resolution']['url']				
				image_name = InstaApi.save_image(image_url, image_predic_folder)
				image_urls_list.append(image_name)


			print('Saving images complete')
			return image_urls_list
		except Exception as Ex: 
			logger.error("Exception Occurred in:" + METHOD_NAME + "|Exception:" + str(Ex))

	def insta_getlikedmedia():
		METHOD_NAME = "insta_getlikedmedia"
		try:
			access_token = config_json['InstagramApi']['AccessToken']
			logger.debug('Inside: ' + METHOD_NAME)
			str_url = "https://api.instagram.com/v1/users/self/media/liked?access_token={1}"
			api_response = InstaApi.insta_getcall(str_url = str_url, b = access_token)
			return api_response
		except Exception as Ex: 
			logger.error("Exception Occurred in:" + METHOD_NAME + "|Exception:" + str(Ex))		


	def insta_getcall(str_url, a = '', b = '', c = '', d = '', e = '', f = '', g = '', h = '', i = '', j = ''):
		METHOD_NAME = "insta_getcall"
		try:
			logger.debug('Inside ' + METHOD_NAME)
			str_url = str_url.replace("{0}",a)
			str_url = str_url.replace("{1}",b)
			str_url = str_url.replace("{2}",c)
			str_url = str_url.replace("{3}",d)
			str_url = str_url.replace("{4}",e)
			str_url = str_url.replace("{5}",f)
			str_url = str_url.replace("{6}",g)
			str_url = str_url.replace("{7}",h)
			str_url = str_url.replace("{8}",i)
			str_url = str_url.replace("{9}",j)

			logger.debug('Before getting data:' + str_url)
			resp = requests.get(str_url)

			if resp.status_code != 200:
				#something went wrong
				logger.error("Unable to get the user's recent media for the given user name | content: "+ str(resp.content) + '|status code' + str(resp.status_code))
				return ""

			api_response = json.loads(resp.content)
			# logger.debug("Json Response loaded", str(api_response))
			return api_response
		except Exception as Ex: 
			logger.error("Exception Occurred in:" + METHOD_NAME + "|Exception:" + str(Ex))

	