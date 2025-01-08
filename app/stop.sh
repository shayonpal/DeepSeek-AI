#!/bin/bash

if [ -f logs/app.pid ]; then
    pid=$(cat logs/app.pid)
    kill $pid
    rm logs/app.pid
    echo "DeepSeek Chat stopped"
else
    echo "No PID file found"
fi 