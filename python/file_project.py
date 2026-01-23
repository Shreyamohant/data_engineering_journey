from datetime import datetime

file_path = "/Users/shrejalmohanty/Documents/data.txt"

current_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"The Current Time: {current_log}")
print("-" * 40)

try:
    with open(file_path, "r") as f:
        lines = f.readlines()

    cleaned_lines = []
    
    for i in lines:
        stripped = i.strip()
        if stripped:
            clean_line = " ".join(stripped.split())
            cleaned_lines.append(clean_line)
    clean_file_path = "/Users/shrejalmohanty/Documents/clean_data.txt"
    with open(clean_file_path,"w")as f:
        for n in cleaned_lines:
            f.write(n+"\n")
    log_path = "/Users/shrejalmohanty/Documents/log.txt"
    with open(log_path,"w")as f:
        f.write(f"{current_log}-File cleaned succesfully")

        

    print("The Item list is:")
    for x in cleaned_lines:
        print(x)

except FileNotFoundError:
    print("Oops! The file was not found.")
    print("Please check if 'data.txt' exists in the Documents folder.")

