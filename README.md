# FastAPI_hw

Автор: Ларченков Михаил

Описание задания: реализовать микросервис для хранения и обновления информации о собаках для ветеринарной клиники

Микросервис развернут на публичном хостинге https://render.com/ - https://dog-api-1ag6.onrender.com

Реализованы эндпоинты:

1. "GET /" - для корневого маршрута, который возвращает успешный ответ;
   
2. "POST /post" - для добавления временных меток (с проверкой на уникальность и корректность времени);

3. "GET /dog" - для получения списка собак (с опциональной фильтрацией по типу собаки);

4. "POST /dog" - для создания новой записи о собаке (с проверкой на уникальность первичного ключа);

5. "GET /dog/{pk}" - для получения информации о конкретной собаке по её первичному ключу;
   
6. "PATCH /dog/{pk}" - для обновления данных о собаке по её первичному ключу.

### Update # 1

Добавлен Докер файл
![image](https://github.com/garotar/FastAPI_hw/assets/89791114/31073702-323e-48e4-bfef-3958b676bcc8)

![image](https://github.com/garotar/FastAPI_hw/assets/89791114/51fcc0dc-9062-44b5-afd9-1bd863458a99)


