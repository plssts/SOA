#!/bin/bash
tput cup 0 0
tput ed

#echo -ne "\e[36mCreating a user-based network bridge\e[39m"
docker network create ws_bridge
#tput cup 0 36
#echo -e "\e[36m. Done.\e[39m\e[K"

#cd WebServices/Pirmas
#echo -e "\e[?1049h"
#tput cup 0 0
#echo -e "\e[36mCreating a user-based network bridge. Done.\e[39m"
#echo -e "\e[36mLaunching user service\e[39m"
#echo -e "\e[3;15r"
#tput cup 2 0
docker-compose up --build --force-recreate -d
#echo -e "\e[?1049l"
#tput cup 1 0
#tput ed
#echo -e "\e[36mLaunching user service. Done.\e[39m"
#tput cup 2 0
#tput ed
#cd ..
#cd ..
#echo -e "\e[?1049h"
#tput cup 0 0
#echo -e "\e[36mCreating a user-based network bridge. Done.\e[39m"
#echo -e "\e[36mLaunching user service. Done.\e[39m"
#echo -e "\e[36mLaunching conference service\e[39m" 
#echo -e "\e[4;15r"
#tput cup 3 0 
#docker-compose up --build --force-recreate -d
#echo -e "\e[?1049l"
#tput cup 2 0
#tput ed
#echo -e "\e[36mLaunching conference service. Done.\e[39m"
#tput cup 3 0
#tput ed
echo -e "\e[32mReady\e[39m"
