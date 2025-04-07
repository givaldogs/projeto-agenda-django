sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install build-essential -y

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 python3.11-venv -y

sudo apt install nginx -y
sudo apt install certbot python3-certbot-nginx -y
sudo apt install postgresql postgresql-contrib -y
sudo apt install libpq-dev -y
sudo apt install git -y

# Configurando o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Criando as pastas do projeto e repositório

mkdir ~/agendarepo ~/agendaapp

# Configurando os repositórios

cd ~/agendarepo
git init --bare
cd ..
cd ~/agendaapp
git init
git remote add agendarepo ~/agendarepo
git add .
git commit -m 'Initial'
git push agendarepo main -u # erro

# No seu computador local
# git remote add agendarepo windows-agenda@34.57.178.99:~/agendarepo

git remote add agendarepo usuario@IP_SERVIDOR:~/agendarepo
git push agendarepo main

# Configurando o Postgresql
sudo -u postgres psql

postgres=# create role usuario_agenda with login superuser createdb createrole password 'senha_usuario_agenda';
CREATE ROLE
postgres=# create database base_de_dados with owner usuario_agenda;
CREATE DATABASE
postgres=# grant all privileges on database base_de_dados to usuario_agenda;
GRANT
postgres=# \q

sudo systemctl restart postgresql

# Criando o local_settings.py no servidor
nano ~/agendaapp/project/local_settings.py

# Configurando o Django no servidor   (parei aqui dia 20.03.2025) começar daqui
cd ~/agendaapp
python3.11 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install django
pip install pillow
pip install gunicorn
pip install psycopg
pip install faker

python manage.py runserver
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser

# Permitir arquivos maiores no nginx
sudo nano /etc/nginx/nginx.conf

# Adicione em http {}:
client_max_body_size 30M;
sudo systemctl restart nginx