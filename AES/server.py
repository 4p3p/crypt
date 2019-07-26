#/usr/bin/python

from Crypto.Cipher import AES

from select import select

import sys

INTRO = """
El Oracle Padding Attack es algo basico.

OK?

"""

flag = "bs1d3s{th0u_sh4llt_n0t_us3_ECB!}"

key = "estaeslallavedecifradoempleada!!"


if __name__ == '__main__':

    padc = 'F'

    assert (len(flag) == 32) and (len(key) == 32)

    cipher = AES.new(key, AES.MODE_ECB)

    sys.stdout.write(INTRO)
    sys.stdout.flush()

    while True:
        try:
            sys.stdout.write('Ingresa un texto: ')
            sys.stdout.flush()

            rlist, _, _ = select([sys.stdin], [], [])

            inp = ''
            if rlist:
                inp = sys.stdin.readline().rstrip('\n')

            plaintext = inp + flag
            l = len(plaintext)

            padl = (l // 32 + 1)*32 if l % 32 != 0 else 0

            plaintext = plaintext.ljust(padl, padc)

            sys.stdout.write('Aqui tiene su texto cifrado:\n{}\n\n'.format((cipher.encrypt(plaintext)).encode('hex')))
        except KeyboardInterrupt:
            exit(0)