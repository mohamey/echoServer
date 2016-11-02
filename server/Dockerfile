FROM php:7.0-cli
# Copy in all local files to the docker image
COPY . /usr/src/myapp

# Change working directory and run the server
WORKDIR /usr/src/myapp
CMD ["php", "-S", "0.0.0.0:8000", "-t", "."]
