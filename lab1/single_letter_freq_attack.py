freq_table = ['E','T','A','O','I','N','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z']

def find_freq(plain_text):
    frequency = {}
    for letter in plain_text:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    # print(frequency)

    max_freq_letter,max_freq = 0,0
    for letter,freq in frequency.items():
        if freq > max_freq:
            max_freq_letter = letter
            max_freq = freq

    return max_freq_letter

def decrypt(plain_text):
    max_freq = find_freq(plain_text)
    for letter in freq_table:
        shift = int(ord(max_freq) - ord(letter)) % 26 + 1

        decrypted_text = ''
        for i in plain_text:
            decrypted_text += chr((ord(i) + shift) % 26 + 65)

        print(letter + ": " + decrypted_text)


def main():
    plain_text = 'PXPXKXENVDRUXVTNLXHYMXGMAXYKXJNXGVRFXMAHWGXXWLEHGZXKVBIAXKMXQM'
    decrypt(plain_text)

main()




