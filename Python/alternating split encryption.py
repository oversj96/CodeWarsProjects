def encrypt(text, n):
    if(n <= 0 or text is None or text == ""):
        return text
    while(n > 0):
        i = 0
        text = list(text)
        half_one = ""
        half_two = ""
        end_char = ""
        if (len(text) % 2 != 0):
            end_char = text[len(text)-1]
        while(i < len(text) and n is not 0):
            if((i+1) % 2 == 0):
                half_one = half_one + text[i]
                half_two = half_two + text[i-1]
            i += 1
        n -= 1
        text = half_one + half_two + end_char
    return text


def decrypt(text, n):
    if(n <= 0 or text is None or text == ""):
        return text
    while(n > 0):
        i = 0
        length = len(text)
        text = list(text)
        end_char = ""
        if (len(text) % 2 != 0):
            end_char = text[len(text)-1]
        pieces = (text[(len(text)//2):(len(text))])
        text = text[0:len(text)//2]
        decrypted = ""
        for i in range(0, len(text)):
            decrypted = decrypted + (pieces[i]) + (text[i])
        text = decrypted + end_char
        n -= 1
    return text
    # if(len(decrypted) < length):
    #         decrypted = decrypted + pieces[len(pieces)-1]
    # if(n > 1):
    #     return decrypt(decrypted, n-1)
    # else:
    #     return decrypted

val = encrypt("This is a test!", 2)
print(val)
print(decrypt(val, 2))