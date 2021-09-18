import base58, ecdsa, hashlib, ctypes

def address_to_pubkeyhash(address: str) -> bytes:
    pubkeyhash = base58.b58decode(address)[1:-4]
    return pubkeyhash


def wif_to_privkey(wif: str) -> bytes:
    privkey = base58.b58decode(wif)
    return privkey[1:-5]


def pubkey_to_pubkeyhash(pubkey: bytes) -> bytes:
    pubkeyhash = hashlib.sha256(pubkey).digest()
    pubkeyhash = hashlib.new('ripemd160', pubkeyhash).digest()
    return pubkeyhash


def scriptpubkey(pubkeyhash: bytes) -> bytes:
        OP_DUP = bytes.fromhex('76')
        OP_HASH160 = bytes.fromhex('a9')
        OP_PUSHBYTES_20 = bytes.fromhex('14')
        OP_EQUALVERIFY = bytes.fromhex('88')
        OP_CHECKSIG = bytes.fromhex('ac')
        return OP_DUP + OP_HASH160 + OP_PUSHBYTES_20 + pubkeyhash + OP_EQUALVERIFY + OP_CHECKSIG


def doubleSHA256(data: bytes) -> bytes:
    hash1 = hashlib.sha256(data).digest()
    hash2 = hashlib.sha256(hash1).digest()
    return hash2







if __name__ == '__main__':
    input_sk = ecdsa.SigningKey.from_string(wif_to_privkey('cVWFRUfyBA3v6Yr4qnBs5VfWy65kQSrQJrV553xrBspigtzSUFtm'), curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256)
    input_pubkey = input_sk.verifying_key
    input_uncompressed_pubkey = input_pubkey.pubkey.point.to_bytes(encoding='uncompressed')
    input_compressed_pubkey = input_pubkey.pubkey.point.to_bytes(encoding='compressed')
    input_pubkey_hash = pubkey_to_pubkeyhash(input_compressed_pubkey)


    output_sk = ecdsa.SigningKey.from_string(wif_to_privkey('cThPh4BzSr2VHArHDwPFKJW7yJnGyrLjsVVLr1QjkrrV28TLduFe'), curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256)
    output_pubkey = output_sk.verifying_key
    output_uncompressed_pubkey = output_pubkey.pubkey.point.to_bytes(encoding='uncompressed')
    output_compressed_pubkey = output_pubkey.pubkey.point.to_bytes(encoding='compressed')
    output_pubkey_hash = pubkey_to_pubkeyhash(output_compressed_pubkey)


    version = bytes(ctypes.c_int32(1))
    tx_in_count = bytes(ctypes.c_uint8(1))
    tx_out_count = bytes(ctypes.c_uint8(1))
    lock_time = bytes(ctypes.c_uint32(0))

    value_output = bytes(ctypes.c_int64(90000))
    pk_script_output = scriptpubkey(output_pubkey_hash) 
    pk_script_bytes_output = bytes(ctypes.c_uint8(len(pk_script_output)))

    txout = value_output + pk_script_bytes_output + pk_script_output

    hash_previous_transaction = bytes(reversed(bytearray.fromhex('9f0e95ca1649929f3aea5a10ea54c08a899af09339726fbf33f30d81422bae8e')))
    vout = bytes(ctypes.c_uint32(0))
    previous_output = outpoint = hash_previous_transaction + vout
    signature_script = scriptpubkey(input_pubkey_hash)
    script_bytes = bytes(ctypes.c_uint8(len(signature_script)))
    sequence = bytes(ctypes.c_uint32(0xffffffff))

    txin = previous_output + script_bytes + signature_script + sequence

    sighash = bytes(ctypes.c_uint32(1))


    unsigned_transaction = version + tx_in_count + txin + tx_out_count + txout + lock_time + sighash

    hash256 = doubleSHA256(unsigned_transaction)
    
    sig = input_sk.sign_digest(hash256, sigencode=ecdsa.util.sigencode_der_canonize)
    sighash = bytes(ctypes.c_uint8(1))
    sig += sighash
    sig_bytes = bytes(ctypes.c_uint8(len(sig)))
    input_compressed_pubkey_bytes = bytes(ctypes.c_uint8(len(input_compressed_pubkey)))
    signature_script = sig_bytes + sig + input_compressed_pubkey_bytes + input_compressed_pubkey
    script_bytes = bytes(ctypes.c_uint8(len(signature_script)))

    txin = previous_output + script_bytes + signature_script + sequence

    signed_transaction = version + tx_in_count + txin + tx_out_count + txout + lock_time

    print(signed_transaction.hex())
    









