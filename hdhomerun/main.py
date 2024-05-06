import os
import requests
import sys

url = os.environ["HDHR_LOCAL_URL"]

def get_recordings():
    # https://info.hdhomerun.com/info/dvr_api:deleting_recordings
    all_recorded_file_info = requests.get(f'http://{url}/recorded_files.json').json()

    unique_recordings = set()

    for recording in all_recorded_file_info:
        unique_recordings.add(recording['Title'])

    for recording_name in unique_recordings:
        print('"' + recording_name + '"')

def delete_recording(title):
    all_recorded_file_info = requests.get(f'http://{url}/recorded_files.json').json()

    deleted_count = 0

    for recording in all_recorded_file_info:
        if recording['Title'] == title:
            episodes = requests.get(recording['EpisodesURL']).json()
    
            for episode in episodes:
                requests.post(url=episode['CmdURL'], params={'cmd':'delete'}).status_code
                deleted_count += 1
    
    print(f'{deleted_count} recording(s) deleted.')

def main():
    try:
        action = sys.argv[1]
    except IndexError:
        print('An action parameter, must be provided.')
        return

    if action == 'get_recordings':
        get_recordings()
    elif action == 'delete_recording':
        try:
            delete_recording(sys.argv[2])
        except IndexError:
            print(f'Action: {action}, requires a recording name input.')
            return
    else:
        print(f'Action: {action}, is not implemented.')

if __name__ == "__main__":
    main()