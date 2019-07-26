from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from binascii import hexlify, unhexlify

def sign(key, message):
    try:
        ECB = AES.new(key, AES.MODE_ECB)
        messageblocks = [message[i:i + 16] for i in range(0, len(message), 16)]
        tag = ECB.encrypt(messageblocks[0])
        for i in range(1,len(messageblocks)):
            tag = ECB.encrypt(strxor(messageblocks[i], tag))
        return hexlify(tag)
    except:
        print("\nModulo 16 por favor!")
        exit()

if __name__ == '__main__':

    flag = "\nbs1d3s{M4C_f0rg3ry!}"
    key = b'MACISLOVEISNTIT?'
    print("\nGenerador de TAGS de autenticacion superseguro")
    print("Rompe esto!")
    print("Presiona 0 para firmar tu mensaje y 1 para intentar romperlo... :D")
    while(True):
        try:
            inp = raw_input("\n")
            if(inp=="0"):
                hex_msg = raw_input("\nMensaje codificado en hexadecimal\n")
                msg = unhexlify(hex_msg)
                hex_tag = sign(key, msg)
                print("\nAqui tienes! El TAG codificado en hexadecimal!")
                print(hex_tag)
            else:
                print("\nAqui vamos... ")
                print("\nDame dos diferentes mensajes que puedan generar el mismo TAG!")
                msg1 = unhexlify(raw_input("\nMensaje #1: \n"))
                msg2 = unhexlify(raw_input("\nMensaje #2: \n"))
                if(msg1 == msg2):
                    print("\nNo hagas trampa!!")
                    exit()
                if(msg1 != msg2 and sign(key, msg1)==sign(key, msg2)):
                    print(flag)
                    exit()
                else:
                    print("\nNo! :(")
                    exit()
        except:
            exit()