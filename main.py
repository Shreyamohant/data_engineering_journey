from reader import read_all_lines
from logger import log
from validator import is_valid
from clean_data import clean_data
from stats2 import summary
def save_data(filename, lines):
    with open (filename,"w") as f:
        for n in lines:
            f.write(n + "\n")


def main():
    lines = read_all_lines("sample.txt")
    if not lines:
        print("No Data to Process")
        return


    total_lines =0
    valid_count =0
    invalid_count =0
    cleaned_data =[]

    for line in lines:
       total_lines +=1
       if is_valid(line):
          valid_count +=1
          cleaned_data.append(clean_data(line))
       else:
          invalid_count +=1
          log(f"Rejected Line {total_lines}:{line.strip()}")
          
        
  
   
    save_data("clean_data.txt",cleaned_data)
    summary(total_lines, valid_count, invalid_count)
if __name__ == "__main__":
     main()
