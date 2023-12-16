import sys
import ruamel.yaml

def correct_indentation(yaml_content):
    try:
        # Load the YAML content
        data = ruamel.yaml.round_trip_load(yaml_content, preserve_quotes=True)
        
        # Dump the YAML content with correct indentation
        stream = ruamel.yaml.StringIO()
        ruamel.yaml.round_trip_dump(data, stream)
        corrected_yaml_content = stream.getvalue()
        
        return corrected_yaml_content
    except ruamel.yaml.YAMLError as e:
        print(f"Error correcting YAML indentation: {e}")
        return None

# Read the YAML content from file
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    yaml_content = file.read()

# Correct the indentation
corrected_yaml_content = correct_indentation(yaml_content)

# Write the corrected YAML content to file
output_file = sys.argv[2]
with open(output_file, 'w') as file:
    file.write(corrected_yaml_content)
