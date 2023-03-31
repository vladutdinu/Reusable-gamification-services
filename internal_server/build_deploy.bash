docker build -t internal_backend .
docker run -it -d --name internal_backend -p 8000:8000 internal_backend