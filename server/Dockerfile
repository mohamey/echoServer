FROM php:7.0-cli
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
EXPOSE 8000
CMD ["php -S 0.0.0.0:8000 -t", "."]
