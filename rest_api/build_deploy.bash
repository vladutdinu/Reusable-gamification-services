docker build -t rest_api .
docker run -it -d --name rest_api -p 8002:8002 rest_api