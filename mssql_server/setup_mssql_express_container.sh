#!/bin/bash
docker pull mcr.microsoft.com/mssql/server
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
sudo curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install msodbcsql17 -y
sudo apt install unixodbc-dev -y
sudo pip3 install pyodbc
wget ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.7.tar.gz
tar xvzf unixODBC-2.3.7.tar.gz
cd unixODBC-2.3.7/
sudo ./configure --prefix=/usr/local/unixODBC
sudo make
sudo make install
