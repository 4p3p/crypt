def hex_xor(h1, h2):
    i_xor = int(h1, 16) ^ int(h2, 16)
    h_xor = '%032x' % i_xor
    return h_xor

plain1 = '1234567890abcdef1234567890abcdef'

cipher1 = 'de137c2819172a7c4f7c30e384967e38'

plain2 = plain1 + hex_xor(cipher1, plain1)

print("Envia "+plain2)