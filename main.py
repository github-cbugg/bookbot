import string
d = dict.fromkeys(string.ascii_lowercase, 0)

def print_sorted(dict_sorted):
    first_word = "The '"
    second_words = "' character was found"
    third_word = "times"

    for each in dict_sorted:
        print(first_word + each + second_words, dict_sorted[each], third_word)
        #print(dict_sorted)

def sort(dict):
    length = len(dict)
    current_biggest = 0
    biggest_position = 0
    sorted_dictionary = {}
    for i in range(0, length):
        for each in dict:
            if dict[each] > current_biggest:
                current_biggest = dict[each]
                biggest_letter = each
        sorted_dictionary[biggest_letter] = current_biggest
        dict.pop(biggest_letter)
        current_biggest = 0
    return sorted_dictionary

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()

    #this printed out the entire book
    #print(file_contents)

    #this printed out the number of words in the file
    #word_array = file_contents.split()
    #print(len(word_array))

    #This populates the dictionary with the count of each character
    number_of_characters = len(file_contents)
    for i in range(0,number_of_characters):
        character = file_contents[i]
        if character in d:
            d[character] += 1

    arranged_dictionary = sort(d)
    print_sorted(arranged_dictionary)

    #This prints the dictionary with the count
    #print(d)

main()