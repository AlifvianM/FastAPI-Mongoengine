# FastAPI-Mongoengine
this repo is a CRUD server using FastAPI, mongodb, and docker. 
## System requirements
 - python 3.7 or latest: [python](https://www.python.org/)
 - docker: [docker](https://docs.docker.com/engine/install/)
 - poetry: [python poetry](https://python-poetry.org/docs/#installation)
## Setup environment
follow this guide to install
  * install [python](https://www.python.org/)
  * install [docker](https://docs.docker.com/engine/install/) (highly recommend install docker desktop version)
  * install [poetry](https://python-poetry.org/docs/#installation) in your terminal
  * Clone the repo: ```git clone https://github.com/AlifvianM/FastAPI-Mongoengine.git``` then ```cd FastApi-Mongoengine```
  * type ```poetry config virtualenvs.in-project true```. this command will create a virtualenv in your working folder
  * install with poetry : ```poetry install```
  
 ## Run Server 
 after installing using ```poetry install```, it's all ready to run with
 ```uvicorn app.main:app``` if you want to run it localy but dont forget to install [mongodb](https://docs.mongodb.com/manual/installation/)
 
 ## Run Server Via Docker Compose
 this repo include ```Dockerfile``` and ```docker-compose.yml``` and it can be installed with this steps
  - ```docker-compose up -d --build```
