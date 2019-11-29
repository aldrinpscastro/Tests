from hashlib import sha256
from base58 import b58encode
from binascii import unhexlify
versao = '80'
chavePrivada = sha256(b'Não').hexdigest()
versaoEchavePrivada = versao + chavePrivada
print(versaoEchavePrivada)
primeiroSHA = sha256(versaoEchavePrivada.encode()).hexdigest()
print(primeiroSHA)
segundoSHA = sha256(primeiroSHA.encode()).hexdigest()
print(segundoSHA)
WIF = b58encode(unhexlify((versaoEchavePrivada + segundoSHA[:8])))
print(WIF)
