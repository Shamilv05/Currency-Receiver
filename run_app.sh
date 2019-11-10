docker-compose  -f docker-compose.yml rm -fsv
docker-compose  -f docker-compose.yml build --pull
docker-compose  -f docker-compose.yml up --remove-orphans --exit-code-from=app app
docker-compose  -f docker-compose.yml rm -fsv
