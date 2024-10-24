#!/usr/bin/env bash

export IMAGE_TAG=$1
cd /home/ec2-user/advanced-project
docker-compose -f docker-compose.yaml up --detach
