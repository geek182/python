# create to resolve this puzzle
# http://www.pythonchallenge.com/pc/def/map.html
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

phrase = (list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"))
translate = ""
for letter in phrase:
    if letter == "y":
        word = alphabet.index(letter) - 24
        translate += alphabet[word]
    elif letter == "z":
        word = alphabet.index(letter) - 24
        translate += alphabet[word]
    elif letter =="(":
        word = "("
        translate += word
    elif letter ==")":
        word = ")"
        translate += word
    elif letter == " ":
        translate += " "
    elif letter == ".":
        translate += "."
    else:
        word = alphabet.index(letter) + 2
        translate += alphabet[word]

print translate
