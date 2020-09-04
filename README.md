# easyBox
###### A custom selenium Docker container that disables the firewall of the Vodafone Station. Because the firewall blocks some content that should not be blocked The firewall can only be shutdown for 24h. To fix this just run the container every 24h.

## How to Use

### Install Docker
If you have not already installed docker you have to install it.
```
curl -fsSL https://get.docker.com | sh
```

### Build the container with Docker
First clone this repository.
```
git clone https://github.com/techtasie/easyBox
cd easyBox
```
\
To Build the container run
```
docker build . --build-arg PASSWORD=CREDENTIALS -t easybox
```
```easybox``` is the name of the container that will be build. **REPLACE** ```CREDENTIALS``` with your password for your easybox login.

### Run the container
To run the container and don't let anything behind just run.
```
docker run --rm easybox
```

## Run this every 24h
### Setup Crontab
**NOTE:** you need to have crontab installed and enabled.

Run the following to edit the crontab file.
```
sudo crontab -e
```
and add to the end of the file:
```
0 6 * * * docker container run --rm easybox >/dev/null 2>&1
```
where 0 6 means it runs every morning at 6 am.
