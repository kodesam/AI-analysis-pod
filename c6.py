def correct_indentation(input_file, output_file):
    try:
        # Create YAML instance
        yaml = ruamel.yaml.YAML()

        # Load the YAML content from input file
        with open(input_file, "r") as file:
            yaml_content = file.read()
            data = yaml.load(yaml_content)

        # Dump the YAML content with correct indentation
        stream = ruamel.yaml.StringIO()
        yaml.dump(data, stream)

        corrected_yaml_content = stream.getvalue()

        # Show the corrected lines of indentation
        diff = difflib.unified_diff(yaml_content.splitlines(keepends=True),
                                    corrected_yaml_content.splitlines(keepends=True),
                                    n=0)

        diff_lines = [line for line in diff if line.startswith("+")]

        st.subheader("Corrected Indentation:")
        if diff_lines:
            for line in diff_lines:
                st.code(line[1:], language="yaml")
        else:
            st.info("No indentation corrections were made.")

        # Write the corrected YAML content to the output file
        with open(output_file, "w") as file:
            file.write(corrected_yaml_content)

        st.success(f"YAML indentation corrected! You can download the output file below.")
