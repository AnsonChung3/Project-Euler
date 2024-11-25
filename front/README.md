# Project Euler Solutions

This is a collection of solutions for math problems using Python. It has both frontend and backend. Answer would come up with a click of a button on frontend.

## Frontend
Simply run the two commands below, and the frontend will be ready :)
```
npm insatall
quasar dev
```

## Backend
With Docker, presuming the frontend is running on 8080, run
```
docker build -t anson_euler .
docker run --name anson_euler_container -d -p 8181:8080 anson_euler
```
8181 is a solid requirement to run this project because it's configed in quasar.conf.js (under devServer)

When done, easy stop and clean up, run
```
docker kill anson_euler_container && docker rm anson_euler_container
```