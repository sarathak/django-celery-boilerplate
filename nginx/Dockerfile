FROM nginx:1.19.10-alpine
WORKDIR /app
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
ADD . .

#CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "wsgi"]