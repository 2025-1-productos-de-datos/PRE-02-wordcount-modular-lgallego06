# obtain a list of files in the input directory

from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_word_counts import write_word_counts
# obtain a list of files in the input directory
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        sys.exit(1)
        
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    ## mover a la funcion "read_all_lines"
    all_lines = read_all_lines(input_folder)

    ## mover a "preprocess_lines"
    all_lines = preprocess_lines(all_lines)

    ## mover "split_in_words"
    words = split_into_words(all_lines)

    ## mover a "count_words"
    counter = count_words(words)

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    ##
    write_word_counts(counter,output_folder)

if __name__ == "__main__":
    main()
