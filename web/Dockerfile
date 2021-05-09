FROM python:3.8-alpine
WORKDIR /app
RUN apk add gcc libc-dev linux-headers musl-dev zlib zlib-dev postgresql-dev postgresql-client
RUN mkdir static
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

#CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "wsgi"]