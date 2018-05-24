# SendTank Backend

## Development Installation

### 1. Install

```
mkdir project
cd project
virtualenv -p python3 env # create a virtual environment
source env/bin/activate # Enter the virtual environment
git clone git@gitlab.com:awecode/sendtank-backend.git # git clone the repo
cd app # cd to app dir
pip install -r requirements/dev.txt # install Python packages required for development
cp mccc/settings/env.sample.py mccc/settings/env.py # create local settings file from sample file
vi mccc/settings/env.py # configure your settings here, database, static & media paths and urls
./manage.py migrate # synchronize database and run migrations
```

### 2. Run
```
./manage.py runserver
```

### 3. Elastic Installation
Download and install Elasticsearch version **2.4.1**, dependent on Java.

```
curl -L -O https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.1/elasticsearch-2.4.1.tar.gz
tar -xvf elasticsearch-2.4.1.tar.gz
cd elasticsearch-2.4.1/bin
./elasticsearch -d
```

### 4. Redis Installation

Download install redis from package manager.
```
 sudo apt-get install redis-server
 sudo pacman -S redis-server
```

### 5. Start Workers
Go to **project folder**.

```
source env/bin/activate
cd app/
./manage.py qcluster
```

django admin running at [localhost:8000](http://localhost:8000/admin/)

For deployment in production environment, visit [https://motorscript.com/django-deployment-cheatsheet/](https://motorscript.com/django-deployment-cheatsheet/)
