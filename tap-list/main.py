import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
from datetime import datetime

import pytz
import yaml


def get_tap_brewery(spot_filepath, tap_name):
    try:
        with open(spot_filepath, "r") as file:
            data = yaml.safe_load(file)["taps"]

            for tap in data:
                if tap["name"] == tap_name:
                    return tap["brewery"]
            return None
    except FileNotFoundError:
        print(f"Error: File not found at {spot_filepath}")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")


def get_taps(file_path, is_action):
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)["taps"]

            if is_action:
                return [f'"{tap['name']}"' for tap in data]
            return [f"{tap['name']}" for tap in data]

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")


def create_entry(spot_filepath, desc, commit_url):

    central_tz = pytz.timezone("America/Chicago")
    now = datetime.now(central_tz)

    # Format it as a string
    datetime_string = now.strftime("%m/%d/%Y %I:%M %p")

    tree = ET.parse(f"{spot_filepath}/rss.xml")
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
    parser.add_argument("spot", type=str)
    parser.add_argument("-sha", type=str)
    parser.add_argument("-taps", nargs="*")
    args_parsed = parser.parse_args()

    spot_filepath = f"spots/{args_parsed.spot}/tap_list.yaml"

    if args_parsed.action == "rss":
        updated_taps = set(get_taps(spot_filepath, False))
        current_taps = set(args_parsed.taps)

        new_taps = sorted(list(updated_taps - current_taps))
        retired_taps = sorted(list(current_taps - updated_taps))

        if new_taps:
            description = "<br>\nNew Taps:\n<br>"

            for new in new_taps:
                description = f"{description} - {new}, {get_tap_brewery(spot_filepath, new)}\n<br>"

        if retired_taps:
            description = f"{description}\n<br>Retired Taps:\n<br>"

            for old in retired_taps:
                description = f"{description} - {old}\n<br>"

        if not new_taps and not retired_taps:
            description = "No taps were rotated."

        commit_url = (
            f"https://github.com/carlknutson/ios-shortcuts/commit/{args_parsed.sha}"
        )
        create_entry(f"spots/{args_parsed.spot}", description, commit_url)

    elif args_parsed.action == "get_taps":
        print(" ".join(get_taps(spot_filepath, True)))
    else:
        raise
