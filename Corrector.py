import streamlit as st
import yaml
from difflib import Differ

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
        with open('original.yaml', 'wb') as file:
            file.write(uploaded_file.read())
        
        # Correct the spacing
        corrected_yaml = correct_spacing('original.yaml')
        
        if corrected_yaml:
            st.subheader("Difference")
            
            d = Differ()
            diff = list(d.compare(uploaded_file.getvalue().decode('utf-8').splitlines(), corrected_yaml.splitlines()))
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Original YAML")
                st.code(uploaded_file.getvalue().decode('utf-8'))
            
            with col2:
                st.subheader("Corrected YAML")
                st.code(corrected_yaml)
            
            st.subheader("Diff")
            diff_text = ""
            for line in diff:
                if line.startswith('- '):
                    diff_text += f"**{line}**\n"
                elif line.startswith('+ '):
                    diff_text += f"^{line}^\n"
            
            st.text_area("Difference", value=diff_text, height=500)
        else:
            st.sidebar.info("Please upload a valid Ansible Script YAML file.")
    else:
        st.sidebar.info("Please upload an Ansible Script YAML file.")

if __name__ == '__main__':
    main()
