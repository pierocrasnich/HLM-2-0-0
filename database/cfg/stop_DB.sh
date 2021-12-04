#!/bin/bash
#stop  mongoDB

mongo --port 27017 --eval 'db.adminCommand("shutdown")'
mongo --port 27018 --eval 'db.adminCommand("shutdown")'
