def create_KeyTable(key):
    # remove white-spaces
    key = "".join(key.split())
    # convert to lower-case
    key = key.lower()
    # replace all occurences of j with i
    key = key.replace('j','i')
    alphabets = 'abcdefghiklmnopqrstuvwxyz'
    unique = {i for i in key}
    key_len = len(key)
    alphabet_len = 25
    remaining = {j for j in alphabets}
    remaining.symmetric_difference_update(unique)
    # print(unique)
    # print(remaining)
    keyTable = []
    l1,l2 = 0,0
    # print(l1,l2)
    # for i in range(5):
        # temp = []
        # for j in range(5):
            # if l1<key_len and key[l1] not in remaining:
                # temp.append(key[l1])
                # l1  += 1
            # elif l2<alphabet_len and alphabets[l2] in remaining:
                # temp.append(alphabets[l2])
                # l2 += 1
        # keyTable.append(temp)
    i,j = 0,0
    temp = []
    for k in key:
        if k in unique:
            temp.append(k)
            unique.remove(k)
            j += 1
            if j == 5:
                i += 1
                keyTable.append(temp)
                temp = []
                j = 0

    for a in alphabets:
        if a in remaining:
            temp.append(a)
            remaining.remove(a)
            j += 1
            if j == 5:
                i += 1
                keyTable.append(temp)
                temp = []
                j = 0

    return keyTable

def search(a,b,keyTable):
    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'
    pos = [0 for i in range(4)] 
    for i in range(5):
        for j in range(5):
            if keyTable[i][j] == a:
                pos[0] = i
                pos[1] = j
            elif keyTable[i][j] == b:
                pos[2] = i
                pos[3] = j

    return pos

def encrypt(plain_text, key):
    key_table = create_KeyTable(key)

    if len(plain_text)%2 != 0:
        plain_text += 'z'

    cipher = ''

    for i in range(0,len(plain_text),2):
        pos = search(plain_text[i],plain_text[i+1],key_table)
        if pos[0] == pos[2]:
            cipher += key_table[pos[0]][(pos[1]+1)%5]
            cipher += key_table[pos[0]][(pos[3]+1)%5]
        elif pos[1] == pos[3]:
            cipher += key_table[(pos[0]+1)%5][pos[1]]
            cipher += key_table[(pos[2]+1)%5][pos[1]]
        else:
            cipher += key_table[pos[0]][pos[3]]
            cipher += key_table[pos[2]][pos[1]]

    return cipher

def decrypt(cipher, key):
    key_table = create_KeyTable(key)

    plain_text = ''

    for i in range(0,len(cipher),2):
        pos = search(cipher[i],cipher[i+1],key_table)
        if pos[0] == pos[2]:
            plain_text += key_table[pos[0]][(pos[1]+4)%5]
            plain_text += key_table[pos[0]][(pos[3]+4)%5]
        elif pos[1] == pos[3]:
            plain_text += key_table[(pos[0]+4)%5][pos[1]]
            plain_text += key_table[(pos[2]+4)%5][pos[1]]
        else:
            plain_text += key_table[pos[0]][pos[3]]
            plain_text += key_table[pos[2]][pos[1]]

    return plain_text

def main():
    key = "Monarchy"
    message = "instruments"
    print(create_KeyTable(key))
    cipher = encrypt(message, key) 
    print(cipher)
    plain_text = decrypt(cipher, key)
    print(plain_text)

main()
    
            




