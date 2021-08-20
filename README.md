# products_fastapi

1. Установка
pip install -r requirements.txt
Также устанавливаем docker image mongo.

Запускаем контейнер командой docker run -d -p 27017:27017 mongo

Создаем бд product.

2. Запуск
python main.py

3.1 Добавление нового товара
curl -X 'POST' \
  'http://127.0.0.1:8000/product/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "IPhone 11",
  "description": "Released 2019, September 20 · 194g, 8.3mm thickness",
  "parameters": [
    {
      "camera": "12MP"
    },
    {
      "memory": 64
    }
  ]
}'

3.2 Поиск товара по ID
curl -X 'GET' \
  'http://127.0.0.1:8000/product/{id}' \
  -H 'accept: application/json'

*** Вместо {id} подставить ID созданного товара ***

3.3 Поиск товаров по названию
curl -X 'GET' \
  'http://127.0.0.1:8000/product/name/{name}' \
  -H 'accept: application/json'


*** Вместо {name} подставить название товара ***


Пример:
curl -X 'GET' \
  'http://127.0.0.1:8000/product/name/IPhone%2011' \
  -H 'accept: application/json'


3.4 Поиск товаров по параметрам
curl -X 'GET' \
  'http://127.0.0.1:8000/product/params/get?params={query}' \
  -H 'accept: application/json'

*** Вместо {query} подставить параметр товара и его значение в формате ключ-значение в формате JSON ***

Пример:
curl -X 'GET' \
  'http://127.0.0.1:8000/product/params/get?params=%7B%22memory%22%3A64%7D' \
  -H 'accept: application/json'
