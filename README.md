# Echo Client/Server
Source code for Distributed systems Lab 1, where the client has been built into the docker image `mohamey/echoclient` and the server built into the image `mohamey/echoserver`. The client is written in Python, the server is the php file as supplied by Stephen Barrett.

## echoclient
Consists of the one python3 file, `client.py`. It is hard-coded to send the same message "someMessage" to the server every time, and the server is hard-coded to the location of my php server in scssnebula.

### Run Client
To run the client, simply execute the command
```
python3 client.py
```

Or alternatively, you can run the docker image as follows:
```
docker run mohamey/echoclient
```

If you've modified the Dockerfile and wish to rebuild the image, you can do so by changing the working directory to the client directory, and running
```
docker build -t your-dockerhub-profile/echoclient .
```

### Run Server
To run the server, simply change the working directory to the server directory and execute the command
```
php -S 0.0.0.0:8000 -t .
```

Alternatively, you can use my docker image found at `mohamey/echoserver`. To run this, execute the command:
```
docker run -p 8000:8000 mohamey/echoserver
```
This will start the php server and expose the servers port at port 8000 of the host machine.

If you decide to update and rebuild the docker image, it can be done by executing the following command
```
docker build -t your-dockerhub-profile/echoserver .
```

## Running the project
This project has already been deployed to SCSSNebula, but to run it locally simply run:
```
docker run -p 8000:8000 mohamey/echoserver
docker run mohamey/echoclient
```

Please note the echo client is hardcoded to point to my DebianJessie node, so you __will__ need to update the client.py file and rebuild a docker image.

## Docker Image Notes
Just to reiterate the points made above:
* The PHP docker image runs a server that listens on port _8000_. You can expose port 8000 on whatever port you wish on the host machine, however you must modify the client python script if you don't expose the php server on port 8000.
* The python image is hardcoded to send requests to the ip of my DebianJessie node on SCSSNebula.
