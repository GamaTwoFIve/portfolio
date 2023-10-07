import requests
import json
# переменые можно сделать списком
idpet = 19940419
namepet = 'richi'
poroda = 'cat'
status = 'available'
# Пост запрос на создание

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "id": idpet,
  "category": {
    "id": 2,
    "name": poroda
  },
  "name": namepet,
  "status": status
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text, "Добавлен")


#Смена статуса

status = 'Sold'

# PUT запрос

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "id": idpet,
  "category": {
    "id": 2,
    "name": poroda
  },
  "name": namepet,
  "status": status
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text, 'Продан')

#возвращение переменой в исходное состояние
status = 'available'