import requests
import json
url = "https://api.weatherbit.io/v2.0/current?lat=38.5&lon=-78.5&key=cff96ab9574948a39c318e9b6c3831ef&include=minutely"

querystring = {"lat":"38.5","lon":"-78.5"}

headers = {
    'x-rapidapi-key': "b0e0e2263cmsha50e96d375ad81dp145af4jsn7c1765ced274",
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.json())

my_dict = response.json()
print(my_dict)
#time_zone = my_dict['data'][0]['timezone']
#temperature = my_dict['data'][0]['temp']
#print(temperature)
