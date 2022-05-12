**Сервер**

Выполняет регистрацию пользователей
Тестовые аккаунты:

 >email: iskander@gmail.com<br>
 >password: 123

 >email: test@test.com<br>
 >password: 000

Можно зарегистрировать новый аккаунт.

Запуск:<br>
Запускаем терминал в директории `server`
>python -m venv venv

>.\venv\Scripts\activate

>pip install -r requirements.txt

>set FLASK_APP=server_flask_alimov

>flask run

и в браузере зайти на `http://localhost:5000/`

**Клиент**

Многопользовательский чат
Запускаем терминал в директории `client`
>python -m venv venv

>.\venv\Scripts\activate

>pip install -r requirements.txt

Запустить сервер 

>python server_mess.py

A затем запустить `client.py` или `client2.py` (можно оба сразу)

Запускать клиентов нужно с нового терминала предварительно запустив виртуальную среду

>python -m venv venv

>.\venv\Scripts\activate

>python [client.py / client2.py]

Тестовые email and password в верхней шапке, но можно и самому создать новый аккаунт на сайте

Регистрацию проходить на `http://localhost:5000/`, где после запроса сервер вернет name(если правильно вбили)

**Замечание**
1. Если возникнут проблемы проблемы с виртуальным окружением, то советую удалить файлы venv и установить заново. 
2. Бывают иногда проблемы с потоками на сервере чата.