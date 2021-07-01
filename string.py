def rev_sentence(sentence):
    words = sentence.split(' ')

    reverse_sentence = ' '.join(reversed(words))

    return reverse_sentence
if __name__ == "__main__":
    input = "The greatest victory is that which requires no battle"
    print(rev_sentence(input))
