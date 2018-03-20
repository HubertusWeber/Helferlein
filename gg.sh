#! /bin/sh

echo Pulling New Version
cd ~/GitHub/Fefes-Server/
git pull
cd

echo Restarting Server
~/GitHub/Fefes-Server/scripts/restart.sh
