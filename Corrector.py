import streamlit as st
import yaml

def correct_spacing(filename):
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        
        # Dump the corrected YAML content into a string
        corrected_yaml = yaml.dump(data, default_flow_style=False)
        
        # Return the corrected YAML content
        return corrected_yaml
    except yaml.YAMLError as e:
        st.error("Error parsing the YAML file. Please make sure it is a valid YAML file.")

def main():
    st.title("Ansible Script YAML Spacing Corrector")

    # File upload widget
    uploaded_file = st.sidebar.file_uploader("Upload Ansible Script YAML", type=['yml', 'yaml'])
    
    if uploaded_file is not None:
        # Saving uploaded YAML to a temporary file
        with open('temp.yaml', 'wb') as file:
            file.write(uploaded_file.read())
        
        # Correct the spacing
        corrected_yaml = correct_spacing('temp.yaml')
        
        if corrected_yaml:
            # Display the corrected YAML on the screen
            st.text_area("Corrected YAML", value=corrected_yaml, height=500)
    else:
        st.sidebar.info("Please upload an Ansible Script YAML file.")

if __name__ == '__main__':
    main()
