import streamlit as st
import yaml

def correct_spacing(data):
    # Dump the corrected YAML content into a string
    corrected_yaml = yaml.dump(data, default_flow_style=False)
    
    # Return the corrected YAML content
    return corrected_yaml

def main():
    st.title("YAML Spacing Corrector")

    # File upload widget
    uploaded_file = st.sidebar.file_uploader("Upload YAML file", type=['yml', 'yaml'])
    
    if uploaded_file is not None:
        # Read the uploaded YAML file
        yaml_data = yaml.safe_load(uploaded_file)
        
        # Correct the spacing
        corrected_yaml = correct_spacing(yaml_data)
        
        # Display the corrected YAML on the screen
        st.text_area("Corrected YAML", value=corrected_yaml, height=500)
    else:
        st.sidebar.info("Please upload a YAML file.")

if __name__ == '__main__':
    main()
