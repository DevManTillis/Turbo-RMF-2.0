#!/bin/bash
echo "Building MSSQL Express container..."
docker rm ya --force
docker run --name ya -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=P@55w0rd!' -e 'MSSQL_PID=Express' -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest-ubuntu
#echo "Seeding Database on mssql express container..."
#sleep 25
#./seed_mssql_database.py
#echo "Done"
