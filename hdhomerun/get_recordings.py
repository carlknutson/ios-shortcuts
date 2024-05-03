import os
import requests

url = os.environ["HDHR_LOCAL_URL"]

# https://info.hdhomerun.com/info/dvr_api:deleting_recordings
all_recorded_file_info = requests.get(f'http://{url}/recorded_files.json').json()

for recordings in all_recorded_file_info:
    print(recordings['Title'])