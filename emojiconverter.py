message = input("> ")

def emojiNator(message):
    words = message.split(' ')

    # window+.

    emojis = {
        ":)": "😊",
        ":(": "☹",
        ":|": "😐",
        ";)": "😉"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output

print(emojiNator(message))