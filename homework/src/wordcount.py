# obtain a list of files in the input directory
import os

from homework.src.write_count_words import write_count_words
def read_all_lines():
    lines=[]
    input_file_list=os.listdir('data/input/')
    for filename in input_file_list:
        with open('data/input/'+filename) as f:
            lines.extend(f.readlines())
            all_lines = [line.strip() for line in lines]
    return all_lines

def main():
    # obtain a list of files in the input directory
    files_in_input_dir=os.listdir('data/input/')
    ##files_in_input_dir
    ##files_in_input_dir=os.listdir('data/input/')
    ##files_in_input_dir
    
    
    # read all lines
    #all_lines=read_all_lines()
    #preprocess lines
    #split in words
    #count words
    #write count words
    
    # count the frequency of the words in the files in the input directory
    counter={}
    for filename in files_in_input_dir:
        with open('data/input/'+filename) as f:
            for l in f:
                for w in l.split( ):
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1
                
                
    # create the directory output/ if it doesn't exist
    write_count_words(counter)


            
if __name__ == "__main__":
    main()