#!/bin/bash
echo "Stopping services"
docker stop usr_s
docker stop base_s
#echo "Removing user-based network bridge"
#docker network rm ws_bridge
echo "Clearing empty images"
docker container rm usr_s
docker container rm base_s
docker rmi --force $(docker images --filter dangling=true -q --no-trunc)
echo "Done"
