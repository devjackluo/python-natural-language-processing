#import nltk
#nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize


exampleText = "Hello Mr. Bob, what kind of things do you like? If I had a puppy, I would probably eat it. If I had a cat, he'll probably eat me. If I had a girlfriend, I'll probably not be coding right now. Sad life. Am I such a weak creature? I hope not."

# print(sent_tokenize(exampleText))
# print(word_tokenize(exampleText))

for i in word_tokenize(exampleText):
    print(i)




