def reverse_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words into a new sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Test the function
user_input = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(user_input)
print("Reversed sentence:", reversed_sentence)
