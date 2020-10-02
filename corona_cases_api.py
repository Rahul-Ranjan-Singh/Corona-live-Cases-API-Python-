import json
import requests

api_url = "https://api.covid19api.com/summary"
response = requests.get(api_url) 
result = response.json()
all_countries = result['Countries']

for i in range(1,len(all_countries)):
    current_country = all_countries[i]
    country_code = current_country['CountryCode']
    
    if(country_code == 'IN'):
        print("========" , current_country['Country'] , "========")
        print("Total Cases:  " , current_country['TotalConfirmed'])
        print("New Cases in Last 24 hrs:  " , current_country['NewConfirmed'])
        print("Total Deaths:  " , current_country['TotalDeaths'])
        print("New Deaths in Last 24 hrs:  " , current_country['NewDeaths'])
        print("Recovered:  " , current_country['TotalRecovered'])
        print("Newly Recovered in Last 24 hrs:  " , current_country['NewRecovered'])
        print("\nLast Updated: ", current_country['Date'])