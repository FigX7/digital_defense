# Digital Defense Challenge
A Django REST application dockerized with Angular front end.

## Prerequisites 
- python 3.7 or greater installed
- Docker installed
- git installed
- node
- API testing client = pesonal preference

## Set-up
- in Terminal
1. clone repo = ``` https://github.com/FigX7/digital_defense.git ``` 
2. cd into repo root directory
3. run ```docker-compose up``` wait appox 2 mins for boot  up
4. cd into ./front-end
5.  run ```npm install``` wait appox 2 mins for boot  up
5. run ```ng serve --port 3000```
6. open browser to ```http://localhoset:3000```
8. Happy Testing

## API client Insominia
- A endpoint templte is provided with the repo.
- to run
1. open Insmonia
2. import from ```'digital_defense\Insmonia_File\Insomnia_2020-12-04.yam```l


### NOTES
- test are ran on docker deployment please check Terminal for results and coverage report