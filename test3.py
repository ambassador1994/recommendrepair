import nltk as nltk

tokens = nltk.word_tokenize(
'''Need to return the list of rooms with their status since the last version check on GET /rooms?version=<version>, The body of |GET /rooms/version=xxxx| is simply an array containing objects that look just like those you get from |GET /rooms/{token}|? We'd add "token" to the objects, but they'd otherwise be as defined here: https://wiki.mozilla.org/Loop/Architecture/Rooms#GET_.2Frooms.2F.7Btoken.7D'''
)

print(tokens)