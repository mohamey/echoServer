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
