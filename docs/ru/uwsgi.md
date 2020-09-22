sudo apt install uwsgi
sudo apt-get install uwsgi-plugin-python3

virtualenv ..

pipenv shell
pipenv --venv --> uwsgi.ini --> virtualenv =
pip install uwsgi

test
uwsgi --http :8000 --wsgi-file test.py
uwsgi --http :8000 --module mysite.wsgi

Очень удобно все опции, с которыми мы запускаем uWSGI, указать в ini файле, а при запуске передавать только путь к этому файлу.

Запускаем uWSGI:
uwsgi --ini mysite_uwsgi.ini

Режим Emperor
Создаем папку для конфигурационных файлов:
sudo mkdir /etc/uwsgi
sudo mkdir /etc/uwsgi/vassals

Создаем в ней ссылку на mysite_uwsgi.ini:
sudo ln -s /path/to/your/mysite/mysite_uwsgi.ini /etc/uwsgi/vassals/

Автоматичесеий запуск uWSGI после загрузки операционной системы

