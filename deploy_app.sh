#!/bin/bash
########################################
# from https://raw.githubusercontent.com/ariv3ra/python-circleci-docker/master/deploy_app.sh:
# Put this on a Server
# run chmod +x deploy_app.sh to make the script executable
# 
# Execute this script:  ./deploy_app.sh ariv3ra/python-circleci-docker:$TAG
# Replace the $TAG with the actual Build Tag you want to deploy
#
########################################

set -e

DOCKER_IMAGE=$1
CONAINER_NAME="flask-docker-demo"

# Check for arguments
if [[ $# -lt 1 ]] ; then
    echo '[ERROR] You must supply a Docker Image to pull'
    exit 1
fi

echo "Deploying Flask Docker Demo to Droplet"

#Check for running container & stop it before starting a new one
if [[ $(docker inspect -f '{{.State.Running}}' $CONAINER_NAME) = "true" ]]; then
    docker stop $CONAINER_NAME
fi

echo "Starting Flask-docker-demo using Docker Image name: $DOCKER_IMAGE"

docker run -d --rm=true -p 80:8000  --name $CONAINER_NAME $DOCKER_IMAGE

docker ps -a
