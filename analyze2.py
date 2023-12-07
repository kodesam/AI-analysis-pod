import streamlit as st
import re
from colorama import Fore, Style

def analyze_pod_logs(logs):
    log_entries = re.findall(r"(\d+m)\s+(Warning|Normal|ProvisioningFailed|ProvisioningSucceeded)\s+(.*?)\s+persistentvolumeclaim.*?((?:External provisioner is)|(?:failed to provision volume with StorageClass)|(?:There is already))[^\n]*", logs)
    log_entries.sort(key=lambda x: x[0])

    analyzed_logs = []
    for entry in log_entries:
        timestamp, level, message, info = entry

        if level.startswith("Warning"):
            colored_log = f"{Fore.YELLOW}{timestamp} {level}: {message} {info}{Style.RESET_ALL}"
        elif level.startswith("Normal"):
            colored_log = f"{Fore.GREEN}{timestamp} {level}: {message} {info}{Style.RESET_ALL}"
        elif level.startswith("ProvisioningFailed") or level.startswith("ProvisioningSucceeded"):
            colored_log = f"{Fore.CYAN}{timestamp} {level}: {message} {info}{Style.RESET_ALL}"
        else:
            colored_log = f"{Fore.RED}{timestamp} {level}: {message} {info}{Style.RESET_ALL}"

        analyzed_logs.append(colored_log)

    return "\n".join(analyzed_logs)

def main():
    st.title("Pod Log Analyzer")

    # Get the input pod logs from user input in Streamlit
    logs_input = st.text_area("Enter Pod Logs")

    # Analyze the pod logs when the user clicks the "Analyze" button
    if st.button("Analyze"):
        # Perform log analysis
        analysis_result = analyze_pod_logs(logs_input)

        # Display the analysis results in Streamlit
        st.write("Analysis Results:")
        st.write(analysis_result)

if __name__ == "__main__":
    main()
