sentence = input("Enter a sentence: ")
capitalized_sentence = ' '.join(word.capitalize() for word in sentence.split())
print("Capitalized sentence:", capitalized_sentence)
