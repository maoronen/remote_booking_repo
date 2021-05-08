import requests

url = "https://api.weatherbit.io/v2.0/current?lat=34.957317&lon=32.806203&key=ccfc524cb238411c9e49897be51ead2e&include=minutely"

querystring = {"lat":"38.5","lon":"-78.5"}

headers = {
    'x-rapidapi-key': "b0e0e2263cmsha50e96d375ad81dp145af4jsn7c1765ced274",
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)