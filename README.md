docker build -t hotels-data-merge:0.01 .
docker run --name test -p 8000:8000 -d hotels-data-merge:0.01

