import sys
import ruamel.yaml

def correct_indentation(yaml_content):
    try:
        # Create YAML instance
        yaml = ruamel.yaml.YAML()

        # Load the YAML content
        data = yaml.load(yaml_content)

        # Dump the YAML content with correct indentation
        stream = ruamel.yaml.StringIO()
        yaml.dump(data, stream)

        corrected_yaml_content = stream.getvalue()
        return corrected_yaml_content
    except ruamel.yaml.YAMLError as e:
        print(f"Error correcting YAML indentation: {e}")
        return None

# Read the YAML content from file
input_yaml_content = """
- name: Get Custom Operator info
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Execute kubectl get command
      command:
        cmd: "kubectl get customresourcedefinitions"
        register: custom_operators_info

    - name: Print custom operators info
      debug:
        var: custom_operators_info.stdout_lines
"""

# Correct the indentation
corrected_yaml_content = correct_indentation(input_yaml_content)

# Display the corrected YAML content
print(corrected_yaml_content)