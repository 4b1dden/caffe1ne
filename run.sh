#!/bin/sh
terminate_out=">/dev/null"
api_run="python3 app.py $terminate_out &"
wi_run="npm run dev $terminate_out &"

echo "////////// caffe1ne init script //////////"
cd api
eval $api_run
cd ..
cd web_interface
eval $wi_run
cd ..
echo "both servers running"
eval "jobs"

#todo: shutdown processes after terminal session is terminated
