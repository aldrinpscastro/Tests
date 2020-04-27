#!/usr/bin/env python3.6
from hashlib import sha256
from datetime import datetime

for difficulty in range(1,11):

    nonce = 1

    qzeros = '0' * difficulty

    hashear = int(sha256(str(nonce).encode()).hexdigest(), 16)

    target = int(qzeros + 'ffffff' + '0' * (64 - difficulty - len('ffffff')), 16)

    tinicial = datetime.now().timestamp()

    while hashear > target:

        hashear = int(sha256(str(nonce).encode()).hexdigest(), 16)

        nonce += 1

    tfinal = datetime.now().timestamp()

    delta = tfinal - tinicial

    hashear = hashear.to_bytes(32, 'big').hex()

    print(hashear, nonce, delta)
