
# Django Celery Docker Boilerplate 

The Django Celery Docker boilerplate is a project template designed to streamline the development of Django applications that utilize Celery for asynchronous task processing, along with Redis as the message broker. It also includes Docker, a containerization platform, to simplify the deployment and environment setup process.

Key features and components of this boilerplate include:

- Django Framework: Django serves as the foundation for the web application, providing a robust and scalable framework for building Python-based web applications. It offers features such as routing, ORM, authentication, and more.

-  Celery: Celery is an asynchronous task queue library used for executing background tasks or long-running processes. It enables the offloading of time-consuming operations to separate worker processes, ensuring that the main application remains responsive. Celery handles the distribution, queuing, and execution of tasks.

- Redis: Redis is a high-performance in-memory data structure store that serves as the message broker for Celery. It acts as the intermediary between the Django application and Celery workers, facilitating the communication and transfer of tasks and results.

-  Docker: Docker allows for containerization of the entire Django, Celery, and Redis stack. Containers provide a lightweight and isolated environment, ensuring consistent deployment across different systems and simplifying the setup process. Docker enables seamless deployment and eliminates potential compatibility issues.

# start web

    docker-compose up -d

## app url : http://localhost:8080/
## admin url : http://localhost:8080/admin


    
# create super user

    docker exec -it order_web python manage.py createsuperuser

