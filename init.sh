#!/bin/sh
TERMINATE_OUT=">/dev/null"
api_run="python3 app.py $TERMINATE_OUT &"
wi_run="npm run dev $TERMINATE_OUT &"
DEFAULT_SLEEP=1

p () {
    echo "[$(date +"%H:%M")]:" $1
}

cleanup() {
    p "Shutting down web interface"
    sleep 10
    proc="$(sudo lsof -n -i :8080 | grep LISTEN)"
    PID="$(echo $proc | cut -d ' ' -f2)"
    kill -9 $PID > /dev/null
    p "Shutting down API"
    sleep 2
    pkill -P $$
}

cat ascii_art.txt
echo "\n"
p "Launching API..."
sleep $DEFAULT_SLEEP
cd api && eval $api_run && cd ..
sleep $DEFAULT_SLEEP
p "API is running"
sleep $DEFAULT_SLEEP
p "Launching web interface"
sleep $DEFAULT_SLEEP
cd web_interface && eval $wi_run && cd .. 
sleep $DEFAULT_SLEEP
p "Web interface is running"

# echo "TO TERMINATE THIS PROCESS SAFELY, TYPE 'EXIT'"
cleanup