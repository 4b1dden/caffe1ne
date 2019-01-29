import os

PROJECT_NAME = "caffe1ne"
DASHBOARD_INIT_CMD = "npm run --prefix web_interface serve"
API_INIT_CMD = "python3 api/app.py"

print ("///// {} init script /////".format(PROJECT_NAME))

print ("Starting API...")
api_init = os.system(API_INIT_CMD)
print(api_init)

print ("Starting web interface...")
dashboard_init = os.system(DASHBOARD_INIT_CMD)
print(dashboard_init)
