# Instagram-Api-Image-Recognition
Image recognition using tensorflow and instagram api 

Integrating instagram api to fetch images based on the username, fetch images for the given username and on basis of the selected image, tensorflow recognizes the probablity of objects in the images. 
The project uses the sample code provided by tensorflow github through its turotial.

The website is hosted using digitalocean on (http://104.131.45.126:8000) using a ubuntu server and currently only supports my personal username i.e. afsan_gj. 

The project was build using Django 2.0 and deployed with the help of docker. 

The project expects a config.json file and directories static and media/Prediction Images in Instagram-Api-Image-Recognition/InstaImageRecognition/InstaIR/ which were not pushed on git. 
The config format is 
```json
{
	"InstagramApi":{
		"AccessToken":""
	}
}
```
