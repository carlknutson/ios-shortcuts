import yaml

def get_taps(file_path):
  try:
    with open(file_path, 'r') as file:
      data = yaml.safe_load(file)['taps']
      
      return [f'"{tap['name']}"' for tap in data]

  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
  except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")

if __name__ == "__main__":
  yaml_file = "taplist.yaml"
  print(' '.join(get_taps(yaml_file)))
