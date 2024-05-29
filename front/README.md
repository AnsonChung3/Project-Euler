# template (template)

## Backend (copied)
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

## End notes
This is the template for new porjects with JS fronted and Python backend

Frontend: vue 3.0, quasar 2.0, npm 8.5.5, nodejs 16.14.2; 
Backend: python 3, docker only

ver 1.0
fixed eslint rules: 4 space indent; no space before function parenthesis; semi colon at the end; double quotes for strings