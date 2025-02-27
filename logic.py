import pytz
from datetime import datetime
from pathlib import Path
import os

# clean the data present in result.html, as it is a dynamically created file
def delete_file():
    data_folder = Path("templates")
    file_to_delete = data_folder / "result.html"
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)

# Define the desired time zone for normalization
desired_tz = pytz.timezone("Asia/Kolkata")

# Function to normalize date to the desired time zone
def normalize_date(date_str):
    date = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y %z")
    return date.astimezone(desired_tz)


# function which takes string as input and returns the sorted hash map of (commit, Date)
def compute(content, isDateRequired):
    # dictionary to store {commit_id, date}
    if isDateRequired:
        commits = {}
    else:
        commits = set()

    # list of strings where each string is a complete line in the file
    content_line_wise = content.split("\n")

    for i in range(len(content_line_wise)):
        if content_line_wise[i].startswith("commit"):
            commit_id = content_line_wise[i].strip().split()[1]

            if isDateRequired:
                # having stored the current commit id, we search for the current date of the commit id
                for j in range(i, len(content_line_wise)):
                    if content_line_wise[j].startswith("Date:"):
                        date_str = content_line_wise[j].strip().replace("Date:   ", "")
                        normalizedDate = normalize_date(date_str)
                        commits[commit_id] = normalizedDate
                        break
            
            else:
                commits.add(commit_id)
    
    return commits


# function to find the commits present in content1, and not in content2
def findDifference(content1, content2):
    result = {}

    for key1,value1 in content1.items():
        isPresent = False
        for key2 in content2:
            if key1 == key2:
                isPresent = True
                break
        
        if isPresent == False:
            result[key1] = value1
    
    # finally having the result, we just sort the dictionary as per the date
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))
    print(sorted_result)
    return sorted_result


# function that stores final_result to be passed to html
def saveContents(sorted_result, file1, file2):
    output_file_path = 'output.txt'

    fp = open(output_file_path, "w")
    fp.write("List of commits present in {} and not present in {}\n".format(file1.filename, file2.filename))

    for key,value in sorted_result.items():
        fp.write("{}\t{}\n".format(key, value))

    fp.close()
