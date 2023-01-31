from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.http import HttpResponse
import requests
import json

def home(request):
	if request.method=='POST':
		country=request.POST['country']
		url='http://api.weatherstack.com/current?access_key='API_KEY'&query=country'
		params={ 'access_key':'API_KEY','query': 'country'}
		response=requests.get(url,params=params)
		response_dict=response.json()
		# response_name = response_dict["location"]["name"],["location"]["country"]
		temperature=response_dict["current"]["temperature"]
		wind_speed = response_dict["current"]["wind_speed"]
		weather_icons=response_dict["current"]["weather_descriptions"][0]
		weather_temperature=response_dict["current"]["temperature"]
		response_string = "temperature :"+str(temperature)  +" wind_speed :"+str(wind_speed) +" weather_icons:"+str(weather_icons)+"Temperature:"+str(weather_temperature)+"C"


		
		
		print(response.json())
		return HttpResponse(response_string)
		
	return render(request,'weatherApp/home.html')



