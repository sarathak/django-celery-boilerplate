# start web

    docker-compose up -d

## app url : http://localhost:8080/
## admin url : http://localhost:8080/admin


    
# create super user

    docker exec -it order_web python manage.py createsuperuser

