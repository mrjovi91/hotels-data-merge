docker build -t hotels-data-merge:0.01 .
docker run --name "hotels-data-merge" -p 127.0.0.1:8000:8000 -d hotels-data-merge:0.01

