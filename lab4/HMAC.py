from SHA1 import SHA1HASH

class HMAC:

    def __init__(self, key, message, hash_h=SHA1HASH):

        self.i_key_pad = bytearray()
        self.o_key_pad = bytearray()
        self.key = key
        self.message = message
        self.blocksize = 64
        self.hash_h = hash_h
        self.init_flag = False

    def init_pads(self):

        for i in range(self.blocksize):
            self.i_key_pad.append(0x36 ^ self.key[i])
            self.o_key_pad.append(0x5C ^ self.key[i])

    def init_key(self):

        if len(self.key) > self.blocksize:
            self.key = bytearray(SHA1HASH(key).final_hash())
        elif len(self.key) < self.blocksize:
            i = len(self.key)
            while i < self.blocksize:
                self.key += b"\x00"
                i += 1


    # To be modified!!!
    # def digest(self):

        # if self.init_flag == False:
            # self.init_key()
            # self.init_pads()

            # self.init_flag = True
        
        # return self.hash_h(bytes(self.o_key_pad) + self.hash_h(bytes(self.i_key_pad) + self.message).digest()).digest()

    def hexdigest(self):

        if self.init_flag == False:

            self.init_key()
            self.init_pads()

            self.init_flag = True

        # print(type(bytes(self.o_key_pad)))
        # print(type(bytes(self.hash_h(bytes(self.i_key_pad) + self.message).final_hash(),"utf-8")))
        return self.hash_h(bytes(self.o_key_pad) + bytes(self.hash_h(bytes(self.i_key_pad) + self.message).final_hash(),"utf-8")).final_hash()

# Driver Code-
# def main():

    # h = HMAC(b"key", b"Hello World", SHA1HASH)
    # key = "key"
    # message = "Hello World"
    # print("Key:" + key)
    # print("Message:" + message)
    # output = h.hexdigest()
    # print("Output Digest:" + output)

# main()
