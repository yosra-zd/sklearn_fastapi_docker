docker build . -t sklearn_fastapi_docker:latest
docker build ./train -t train_image:latest
docker build ./test -t test_image:latest
docker-compose up
