# SendTank Backend

## Development Installation

### 1. Install

```
virtualenv -p python3 env # create a virtual environment
source env/bin/activate # Enter the virtual environment
git clone git@github.com:ankitch/mccc-backend.git app # git clone the repo
cd app # cd to project dir
pip install -r requirements/dev.txt # install Python packages required for development
cp mccc/settings/env.sample.py mccc/settings/env.py # create local settings file from sample file
vi mccc/settings/env.py # configure your settings here, database, static & media paths and urls
./manage.py migrate # synchronize database and run migrations
```

### 2. Run
```
./manage.py runserver
```

### 3. Elastic and Redis Installation

Download and install elasticsearch version **2.4.1** dependant on java

```
curl -L -O https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.1/elasticsearch-2.4.1.tar.gz
tar -xvf elasticsearch-2.4.1.tar.gz
cd elasticsearch-2.4.1/bin
./elasticsearch
```

### 4. Redis Installation

Download install redis from package manager.
```
 sudo apt-get install redis-server
 sudo pacman -S redis-server
```

### 5. Start Workers

```
./manage.py qcluster
```

django admin running at [localhost:8000](http://localhost:8000/admin/)

