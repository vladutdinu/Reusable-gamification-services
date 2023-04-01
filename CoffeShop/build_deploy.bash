docker build -t coffeshop .
docker run -it -d --name coffeshop -p 8001:8001 coffeshop