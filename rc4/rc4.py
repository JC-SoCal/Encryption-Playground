import sys
import os
#v3
 
#RC4 Implementation
def rc4_crypt(data, key):
    S = range(256)
    j = 0
    out = []
    #KSA Phase
    for i in range(256):
        j = (j + S[i] + ord( key[i % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]
    #PRGA Phase
    i = j = 0
    for char in data:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))
        
    return ''.join(out) 

def main():
    # Provide Directory and Key
    if len(sys.argv) != 3:
        print (" Usage: <directory of files> <key> ")
        return 1
    
    directory = sys.argv[1]
    key  = tuple(sys.argv[2]) 
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        f = open(filepath, 'rb')
        while True:
            #Reading 88 bytes at a time
            piece = f.read(88)      
            print filename +", " + rc4_crypt(piece, key).strip()
            #if we are out of data 
            if not piece:
                break
        f.close()


if __name__ == '__main__':
    main()