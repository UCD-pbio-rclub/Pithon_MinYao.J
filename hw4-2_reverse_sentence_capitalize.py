def reverse_sentence(sentence):
    sentence = sentence.lower()
    new_sentence = sentence.split()
    new_sentence.reverse()
    new_sentence_complete = " ".join(new_sentence)
    return new_sentence_complete.capitalize()