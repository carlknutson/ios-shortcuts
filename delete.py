# import requests

# # https://info.hdhomerun.com/info/dvr_api:deleting_recordings

# all_recorded_file_info = requests.get('http://hdhr-<UNIQUE-ID>.local/recorded_files.json').json()

# # http://hdhr-<UNIQUE-ID>.local/recorded_files.json, EpisodesURL
# mass_delete_urls = [

# ]

# for episode_url in mass_delete_urls:
#     episodes = requests.get(episode_url).json()
    
#     for episode in episodes:
#         print(requests.post(url=episode['CmdURL'], params={'cmd':'delete'}).status_code)

print('5 Eyewitness')
print('Canada')