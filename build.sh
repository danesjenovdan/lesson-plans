#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN

# BUILD AND PUBLISH BACKEND
sudo docker build -f backend/Dockerfile -t lesson-plans-backend:latest ./backend
sudo docker tag lesson-plans-backend:latest rg.fr-par.scw.cloud/djnd/lesson-plans-backend:latest
sudo docker push rg.fr-par.scw.cloud/djnd/lesson-plans-backend:latest

# BUILD AND PUBLISH FRONTEND
sudo docker build -f frontend/Dockerfile -t lesson-plans-frontend:latest ./frontend
sudo docker tag lesson-plans-frontend:latest rg.fr-par.scw.cloud/djnd/lesson-plans-frontend:latest
sudo docker push rg.fr-par.scw.cloud/djnd/lesson-plans-frontend:latest
