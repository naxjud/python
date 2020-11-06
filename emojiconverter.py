message = input("> ")
words = message.split(' ')

# window+.

emojis = {
    ":)": "😊",
    ":(": "☹"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)