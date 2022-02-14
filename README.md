# FastAPI-Mongoengine
this repo is a CRUD server using FastAPI, mongodb, and docker. 
## Setup environment
follow this guide to install
  * Clone the repo: ```git clone https://github.com/coreui/coreui-react.git```
  * install with poetry : ```poetry install```
  
 ## Run Server 
 after installing using ```poetry install```, it's all ready to run with
 ```uvicorn app.main:app``` if you want to run it localy but dont forget to install [mongodb](https://docs.mongodb.com/manual/installation/)
 
 ## Run Server Via Docker Compose
 this repo include ```Dockerfile``` and ```docker-compose.yml``` and it can be installed with this steps
  - ```docker-compose up -d --build```
