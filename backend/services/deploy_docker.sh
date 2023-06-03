#!/bin/bash
docker build -t ghp2201/guiame-api:$1 .
docker push ghp2201/guiame-api:$1
