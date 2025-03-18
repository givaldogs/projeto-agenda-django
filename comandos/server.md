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
# git remote add agendarepo givaldogs@34.57.178.99:~/agendarepo

git remote add agendarepo usuario@IP_SERVIDOR:~/agendarepo
git push agendarepo main
