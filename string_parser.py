#!/usr/bin/env python3

# Created by: Sarah
# Created on: June 2nd, 2022.
# This program asks the user to enter a string. It then splits the string up
# into words and displays it to the user.


# this function parse the sentence user enters then returns it
def string_parser(sentence):
    list_of_words = sentence.split(" ")
    return list_of_words


def main():
    # creates an empty list
    list_of_sentence = []

    print("This program will ask the user for a sentence and then")
    print("display each word, without spaces, one per line.")

    # gets user input
    user_str = input("Enter a string: ")

    list_of_sentence.append(user_str)

    # calls function
    final_string = string_parser(user_str)

    print("The words in your sentence, without spaces, are:")

    # displays the parse string to user
    for a_string in final_string:
        print(a_string)


if __name__ == "__main__":
    main()
