import sys
import ruamel.yaml

def correct_indentation(input_file, output_file):
    try:
        # Create YAML instance
        yaml = ruamel.yaml.YAML()

        # Load the YAML content from input file
        with open(input_file, 'r') as file:
            yaml_content = file.read()
            data = yaml.load(yaml_content)

        # Dump the YAML content with correct indentation
        with open(output_file, 'w') as file:
            yaml.dump(data, file)

    except ruamel.yaml.YAMLError as e:
        print(f"Error correcting YAML indentation: {e}")

# Read input and output file paths from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Correct the indentation and write to output file
correct_indentation(input_file, output_file)