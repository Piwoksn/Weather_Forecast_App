from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
  key = '91a016a5ded7f0fd7f29ebb4d50c8090'
  if request.method == 'POST':
    city = request.POST.get('city')
  else:
    city = 'los angeles'
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
  params = {
    "units":"metric",
  }
  data = requests.get(url, params= params).json()
  
  if data:
    day = datetime.date.today()
    desc  = data['weather'][0]['description']
    icon  = data['weather'][0]['icon']
    tem = data['main']['temp']
  
  context = {
    'day': day,
    'city': city,
    'desc': desc,
    'icon': icon,
    'temp': tem
  }
  
  return render(request, 'mainapp/index.html', context)