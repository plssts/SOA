#!/bin/bash
echo "Stopping services"
docker stop usr
docker stop base
echo "Removing user-based network bride"
docker network rm ws_bridge
echo "Clearing empty images"
docker rmi $(docker images --filter dangling=true -q --no-trunc)
echo "Done"
