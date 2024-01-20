import subprocess
import os
import pandas as pd

def git_diff_to_txt(commit_hash, output_folder):
    # Run 'git diff' command for a specific commit hash and capture the output
    git_diff_command = f'git diff {commit_hash}'
    git_diff_output = subprocess.check_output(git_diff_command, shell=True, universal_newlines=True)

    # Create the "water" folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Write the diff output to a text file in the "water" folder
    file_name = os.path.join(output_folder, f'{commit_hash}_diff.txt')
    with open(file_name, 'w') as file:
        file.write(git_diff_output)

    return file_name

def git_log_with_code_changes_and_diff(output_folder):
    # Run 'git log' command and capture the output
    git_log_command = 'git log --pretty=format:"%h|%an|%ad|%s" --date=iso --all'
    git_log_output = subprocess.check_output(git_log_command, shell=True, universal_newlines=True)

    # Split the output into lines
    log_lines = git_log_output.strip().split('\n')

    # Create a list to store log data
    log_data = []

    # Parse each log entry and extract relevant information
    for line in log_lines:
        commit_hash, author, date, message = line.split('|', 3)

        # Write the git diff output to a text file in the "water" folder for each commit
        diff_file = git_diff_to_txt(commit_hash, output_folder)

        log_data.append({
            'Commit Hash': commit_hash,
            'Author': author,
            'Date': date,
            'Message': message,
            'Diff File': diff_file
        })

    # Create a DataFrame from the log data
    df = pd.DataFrame(log_data)

    return df

# Example usage with "water" folder
water_folder = 'water'
git_log_with_diff_dataframe = git_log_with_code_changes_and_diff(water_folder)
print(git_log_with_diff_dataframe)

