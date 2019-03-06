#!/bin/sh
terminate_out=">/dev/null"
api_run="python3 app.py $terminate_out &"
wi_run="npm run dev $terminate_out &"
get_api_process="sudo lsof -n -i :5000 | grep LISTEN"
get_wi_process="sudo lsof -n -i :8081 | grep LISTEN"

echo "////////// caffe1ne init script //////////"
cd api
eval $api_run
cd ..
cd web_interface
eval $wi_run
cd ..
echo "both servers running"
eval "jobs -l"

#todo: shutdown processes after terminal session is terminated
