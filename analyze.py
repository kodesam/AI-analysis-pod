def analyze_pod_logs(logs):
    # Split the logs into individual lines
    log_lines = logs.splitlines()

    # Analysis logic here:
    # You can iterate over the log lines and perform your analysis tasks,
    # such as filtering, parsing, or extracting information

    # Example: Count lines containing a specific keyword
    keyword = "ERROR"
    count = sum(1 for line in log_lines if keyword in line)

    # Example: Extract lines with specific timestamps
    timestamps = [line.split()[0] for line in log_lines if line.startswith("[")]

    # Example: Calculate the total number of log lines
    total_lines = len(log_lines)

    # Return the analysis results
    return {
        "keyword_count": count,
        "timestamps": timestamps,
        "total_lines": total_lines
    }


# Example logs variable for testing
logs = """
[2022-01-01 10:00:00] Error occurred in module A
[2022-01-01 10:01:00] Warning: Invalid input detected
[2022-01-01 10:02:00] Error occurred in module B
[2022-01-01 10:03:00] Operation completed successfully
"""

# Call the analyze_pod_logs function with the logs input
analysis_result = analyze_pod_logs(logs)

# Print the analysis results
for key, value in analysis_result.items():
    print(f"{key}: {value}")
