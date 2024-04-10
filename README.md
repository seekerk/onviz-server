![pylint](https://byob.yarr.is/seekerk/onviz-server/pylint)
# onviz-server
Сервер для сбора данных с камер onviz и рассылки уведомлений в телеграм

## Структура проекта
* [onviz_main](onviz_main) - ядро сервера Django
* [tg_bot](tg_bot) - приложение для запуска бота Telegram. Использует БД сервера для определения получателей сообщений. 
* [ftp_server](ftp_server) - FTP сервер для получения фото/видео данных с камер
* [web_server](web_server) - веб сервер для настройки системы, добавления камер, просмотра данных и т.п.

## Настройка
Для настройки создать файл в `onviz_main/.env`
Допустимые параметры настройки и их дефолтные значения см. в [onviz_main/settings.py](onviz_main/settings.py).