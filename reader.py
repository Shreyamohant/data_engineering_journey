def read_all_lines(filename):
    
    try:
        with open(filename) as f:
            return f.readlines()
    except FileNotFoundError:
       print("File not found")
       return []