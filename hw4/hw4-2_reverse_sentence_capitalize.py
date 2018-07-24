def reverse_sentence(sentence):
    new_sentence = sentence.split()
    new_sentence.reverse()
    new_sentence_complete = " ".join(new_sentence)
    return new_sentence_complete.capitalize()