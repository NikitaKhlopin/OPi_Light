<h1>Современные технологии "Интернет вещей"</h1>

<h2>Состав группы:</h2>
1) Хлопин Никита
2) Тронина Дарья
3) Каменев Владимир

<h2>Описание программы</h2>
К плате OrangePI подключается один светодиод через пины. С помощью фласки написано веб-приложение в котором происходит вкл\выкл сетодиода.

Установка
Установите менеджер пакетов apt-get install python3-pip
Установили venv sudo apt install -y python3-venv
Cоздали виртуальное окружение python3 -m venv venv
Активировали виртуальную среду source env/bin/activate
Выполнили установку пакетов pip install -r requirements.txt
Установили библиотеку OrangePi.GPIO для работы с пинами pip install OrangePi.GPIO
