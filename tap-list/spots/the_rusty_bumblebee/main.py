import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import yaml
from datetime import datetime

def get_taps(file_path, is_action):
  try:
    with open(file_path, 'r') as file:
      data = yaml.safe_load(file)['taps']
      
      if is_action:
        return [f'"{tap['name']}"' for tap in data]
      return [f'{tap['name']}' for tap in data]

  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
  except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")

def create_entry(desc, commit_url):

  # Get the current date and time
  now = datetime.now()

  # Format it as a string
  datetime_string = now.strftime("%d/%m/%Y %I:%M %p")

  tree = ET.parse("rss.xml")
  root = tree.getroot()
  channel = root.find("./channel")

  new_item = ET.Element("item")

  title = ET.SubElement(new_item, "title")
  title.text = datetime_string

  link = ET.SubElement(new_item, "link")
  link.text = commit_url

  description = ET.SubElement(new_item, "description")
  description.text = desc

  channel.append(new_item)

  print(minidom.parseString(ET.tostring(root)).toxml())


if __name__ == "__main__":
  import argparse
  
  parser = argparse.ArgumentParser()
  parser.add_argument("action", type=str)
  parser.add_argument("-sha", type=str)
  parser.add_argument("-taps", nargs="*")
  args_parsed = parser.parse_args()

  if args_parsed.action == 'rss':
    updated_taps = set(get_taps("tap_list.yaml"))
    current_taps = set(args_parsed.taps)

    print(f"updated taps: {updated_taps}")
    print(f"current taps: {current_taps}")

    new_taps = sorted(list(updated_taps - current_taps))
    retired_taps = sorted(list(current_taps - updated_taps))

    descripition = ''
    if new_taps:
      description = 'New Taps:\n'
    
      for new in new_taps:
        description = f'{description} - {new}\n'
    
    if retired_taps:
      description = f'{description}\nRetired Taps'

      for old in retired_taps:
        description = f'{description} - {old}\n'
    
    if not new_taps and not retired_taps:
      description = 'No taps were rotated.'

    commit_url = f'https://github.com/carlknutson/ios-shortcuts/commit/{args_parsed.sha}'
    create_entry(description, commit_url)

  elif args_parsed.action == 'get_taps':
    print(' '.join(get_taps("tap_list.yaml", True)))
  else:
    raise
