from flask import Flask,request,abort
import gnupg
import time
app = Flask(__name__)
gpg = gnupg.GPG(gnupghome="/tmp/gpg")
#gpg = gnupg.GPG(homedir="/tmp/gpg")

couponCodes = {
    "water": "WATER_2019",
    "beer" : "BSIDES{GNUPG_ZLIB_IS_NOT_SECURE}"
}

@app.route("/generateEncryptedVoucher", methods=['POST'])
def generateEncryptedVoucher():

    content = request.json
    (recipientName,drink) = (content['recipientName'],content['drink'])

    encryptedVoucher = str(gpg.encrypt(
        "%s||%s" % (recipientName,couponCodes[drink]),
        recipients  = None,
        symmetric   = True,
        passphrase  = couponCodes[drink]
    )).replace("PGP MESSAGE","DRINK VOUCHER")
    return encryptedVoucher

@app.route("/redeemEncryptedVoucher", methods=['POST'])
def redeemEncryptedVoucher():

    content = request.json
    (encryptedVoucher,passphrase) = (content['encryptedVoucher'],content['passphrase'])

    time.sleep(15)

    decryptedVoucher = str(gpg.decrypt(
        encryptedVoucher.replace("DRINK VOUCHER","PGP MESSAGE"),
        passphrase = passphrase
    ))
    (recipientName,couponCode) = decryptedVoucher.split("||")

    if couponCode == couponCodes["water"]:
        return "Aqui tiene un poco de agua %s\n" % recipientName
    elif couponCode == couponCodes["beer"]:
        return ":D %s! Aqui tiene su codigo: %s\n" % (recipientName, couponCode)
    else:
        abort(500)

if __name__ == "__main__":
    app.run(host='0.0.0.0')