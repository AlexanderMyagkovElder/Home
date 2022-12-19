import requests

response = requests.get('http://mail.ru')
print(response)
city_name = 'Moscow'
API_key = '6f32491a60c040f2ceb91c30e595a544'
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}").text
print(response)


# print(response.json())
#
# temp = response.json()
# temp1 = temp['main']
# print(temp1["temp"])

