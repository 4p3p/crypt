pw="||"
for c in `seq 1 33`; do
    for i in `cat charset`; do
        tmp=$pw;
        tmp+=$i;
        l=`curl -Ns -H 'Content-Type: application/json' -X POST "http://127.0.0.1:5000/generateEncryptedVoucher" --data "{\"recipientName\":\"$tmp\",\"drink\":\"beer\"}" | sed 's/DRINK VOUCHER/PGP MESSAGE/g' | pgpdump | grep 'New:'`;
        echo $i $l;
    done;
    read s;
    pw=$pw$s
done;

