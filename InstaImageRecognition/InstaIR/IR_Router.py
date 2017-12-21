from InstaIR.IR_InstaApi import InstaApi as ia
from InstaIR.IR_Predict import predict_image_main
from InstaIR.Log_Handler import Log_Handler as lh


logger = lh.log_initializer()

class InstaMain:

	def insta_get_images(user_name):
		METHOD_NAME = 'insta_get_images'
		try:
			user_id = ia.insta_getuserid(user_name)
			print("user_id:" + str(user_id))
			recent_media_list = ia.insta_getrecentmedia(user_id)			
			return recent_media_list
		except Exception as Ex: 			
			logger.error("Exception Occurred in:" + METHOD_NAME + "|Exception:" + str(Ex))

	def insta_recog_object(image_name):
		METHOD_NAME = 'insta_recog_object'
		try:
			object_file_details = predict_image_main(image_name)			
			return object_file_details
		except Exception as Ex:
			logger.error("Exception Occurred in:" + METHOD_NAME + "|Exception:" + str(Ex))
		else:
			pass
		finally:
			pass


# InstaMain.insta_router("afsan_gj")