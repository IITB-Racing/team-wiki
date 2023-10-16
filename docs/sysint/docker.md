## Table of contents
* [Why docker?](#why-docker)
* [Working on Linux](#working-on-linux)
* [Working on windows](#working-on-windows)
* [Frequently used commands](#frequently-used-docker-commands)


## Why docker?
Docker is like a virtual environment emulating hardware and software requirements. It builds an image that contains all the required packages for running a certain application. Different computers have different hardwares which can run into different kinds of issues that are hard and cumbursome to debug. Docker helps us with that issue as the hardware and software requirements is also packaged with the application, so if certain application works inside a certain machine with docker then we can be fairly confident that it will work the same on the other machine.
[More info on docker](https://www.docker.com/what-docker#copy1) 

### Current Usages
Currently, docker is implemented inside Github actions ([More info](https://github.com/features/actions)) where we automated the task of checking if any of the update in any subsystem's code isn't breaking the whole codebase. Whenever a new push event occurs in our github repo github actions pulls our pre-built docker image containing all the required dependencies and tries to catkin build the workspace and notifies if any error occurs.

## Working on Linux
### Installation on ubuntu
```sh
sudo apt-get update

sudo apt-get install ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor \ 
			-o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] \
	https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli \
			containerd.io docker-buildx-plugin docker-compose-plugin
```
[Detailed installation](https://docs.docker.com/engine/install/ubuntu/)

## Working on windows
Working on windows is little more easy and GUI based, although I would not recommend using Github desktop unless it is absolutely important 
### Installation on windows
Install the [docker desktop](https://docs.docker.com/desktop/install/windows-install/) application as there is no other way, still don’t use the the application itself just let it run in the background and do all your stuff in the PowerShell, the commands are the same just don't use sudo (also keep docker desktop running in background while using docker)
### Enabling GUI
Firstly you have to install Xming on you PC - [Download Xming](https://sourceforge.net/projects/xming/)
Refer this video for the next steps - [Video Guide](https://youtu.be/BDilFZ9C9mw?t=23) (Warning : this video uses GUI to run docker containers, I would recommend doing it with the terminal)
- Do “docker build .” this will create a new image with display enabled
- Do “docker images” then copy the image id
- Do “docker run -dt —name dv pyrodocker/driverless:base_build bash”
- check if the container is running or not, if not then do “docker start image_name”
- then do “docker exec -it image_name bash”
- source the iitbdv repo too

## Frequently used docker commands

#### *Docker Pull*
Pulls any docker image from docker hub
```sh
sudo docker pull pyrodocker/driverless:base_build
```
[more info on docker pull](https://docs.docker.com/engine/reference/commandline/pull)


#### *Docker Push*
Push the image you have created to your docker hub repository
```sh
sudo docker push [image_tag]:[verison]
```
[more info on docker push](https://docs.docker.com/engine/reference/commandline/push)


#### *Docker run*
It creates a running docker container of the given docker image
```sh
sudo docker run -dt --name dv pyrodocker/driverless:base_build bash
```
Our work requires us to use GUI which is not supported by default, in order to enable it use
```sh
# Enable the xhost using (use this everytime you boot up your computer)
sudo xhost +local:docker
sudo docker run -dt --env="DISPLAY" --env="QT_X11_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --device=/dev/dri:/dev/dri --name dv pyrodocker/driverless:version bash
```
[For windows](#installation-on-windows) the enabling display will be different but much easier

[more info docker run](https://docs.docker.com/engine/reference/commandline/run)


#### *Docker exec*
It enters the running docker container
```sh
sudo docker exec -it dv bash
```
[more info docker exec](https://docs.docker.com/engine/reference/commandline/exec)


#### *Docker start*
It starts the docker container
```sh
sudo docker start dv
```
[more info docker start](https://docs.docker.com/engine/reference/commandline/start)


#### *Docker stop*
It stops the docker container
```sh
sudo docker stop dv
```
[more info docker stop](https://docs.docker.com/engine/reference/commandline/stop)


#### *Docker ps*
It lists out all the running docker containers
```sh
sudo docker ps
```
In order to see both running and stopped docker containers use the -a tag for all
```sh
sudo docker ps -a
```
[more info docker ps](https://docs.docker.com/engine/reference/commandline/ps)


#### *Docker build*
It builds a docker image from the dockerfile
```sh
sudo docker build .
```
[more info dockerfile](https://docs.docker.com/engine/reference/builder/)
[more info docker build](https://docs.docker.com/engine/reference/commandline/build)


#### *Other Commands*
* [sudo docker images](https://docs.docker.com/engine/reference/commandline/images) - lists all the pulled images
* [sudo docker rm dv](https://docs.docker.com/engine/reference/commandline/remove) - deletes a docker container
* [sudo docker rmi pyrodocker/driverless:base_build](https://docs.docker.com/engine/reference/commandline/remove) - deletes an docker image
* [sudo docker tag [current name] [new name]](https://docs.docker.com/engine/reference/commandline/tag) - changes the name of docker container

For more info on different types of commands used in docker refer this -
[Github Cheatsheet](https://github.com/wsargent/docker-cheat-sheet)
