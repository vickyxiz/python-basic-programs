def reverse_sentence(sentence):
    words=sentence.split()
    reversed_words=words[::-1]
    reversed_sentence=" ".join(reversed_words)
    print(reversed_sentence)
sentence=input("enter the sentence:")
reversed_sentence=reverse_sentence(sentence)
