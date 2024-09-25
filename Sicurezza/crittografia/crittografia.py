
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA0yThh9uoOWQD5Go+3B4p6LRR8MOG/0fkMJrCYMbwK3TgLvIa\n/D/QnEtnLSa6CqwQlbL8QzCcLzqdxcux5QCfluwJChG2w87InAo6V/5roFc7BWei\n2sF68qQr3SGriNrHi7+DyYvkyeZfln/ukVFlA+EE2PoGMcP/2BsnW+9Z3mrDFgC+\nC57YOCLiNd1L1Fax9nq9FUuM7AbR3yCNkM/BtPDUrCJFoRkqLEbknVFIUjZyFjjL\n4NQh4yIJ8C73UcHl8bgTxZbzixU9evYyC1lx/RopnFnKpSz+I2LCHINUIcURDQYU\ni8b+zYpqLCJF8ZccLORofuswz6WZ1CfTzKXqBwIDAQABAoIBAFyQb5r6zj4Sva4W\nceZYBvFwk/ekEHu7zasNPaflrwauH1YVZ4UsiMzsNZhSwP7Kvh6SsArYta/y15YO\nHbgSVOR6J+BVMbWX4tSdm0RWUmKhu0s8SuXyKm9TT7OK/kNp/k8ir6jc/nkQ2NkG\nztTARTO1I0XoHm0UywW3qcKhJNnfUjddIEk4K/2UCJP8fO3AcksXlc5wjkWjvwoN\nF1VvRkjE2WOn43Z98T/UUqGrWbs87sPGP90Jb8yFrgTWFiRiXPjSbkrPUX81U2AV\nrVjp0tDFmgdPCrICCIUUnEC2Qk6GqNT8iFBX2b0KWuKImp4dRf2xj7fgP2QwmH1W\nrTf/w8kCgYEA5YGpD7rDtKsvSdrH/R0RklBr7y8piGYKokh4EMAvsWSyjueh97nN\nHUGiR0JmJsoj71+dUSNK90LKgCYsyHRe9VVsuL0rbFCjUwYCfqv0LEHWeCF5YRKp\nEvv7euNuWUCOI2IsyffHnRS0n4zqknEFjuKy3vyioOqot23SswxPY+0CgYEA64ST\nxlEjFk/s1LRj00MvIfy82U3ITZXoU+0fNokEZT7U2qczrNtDv5h3vRWmhMJ0he65\nUGxQ+uK6VIKcIBrxW6E1j2VttWDuDE2c4B+dVofpOHP6vfqCU+2p9+azxy85VwHh\nd961XRk78GlHkaedO3eoUyJ/q2WAEpiFvLpXb0MCgYAjB6ZZS0Vhxxshp64MuSoc\nbf/7cvRg6EpJOMxyqhLdfaQvYbV8DTT8eS8et0jGNOZFPA/T+ZIQqXYlFy6Qrgps\nYcyFagI9txUmr+0jjnVnZ+knTtyq72E1D5bzy9Dk+JB5YBu7/ADQvf9Ptv96uJuD\nkqCAnojoDMkRrkaRo5hehQKBgQC0J2audZQkViDwF8igaqzcD6sZgkEs7/WWdTTC\nD484Lxa85tdFazfokCVPkwccWG6voItKdICBWPt096+bc2CaWbdRqCGCc9HDwX61\nhhlhfncswrLTrZMRxiOUyHlObNYssviYK9iJjWrnHHEtfoxsV7x/U01bezm7f8YV\nNmj5ZwKBgQCpufHKMmrrs0Lndn1+2IqAvCk7OF71t2I6pr6BULfjNPjpGdlv8Pbj\n94xKqQGjGVfmDgaX7ewKD0X1SijOQrLkLcfyRq2n4Y5KNoT9wCDTEob+QoPMuWoA\nYofS/0oz14fGRqbxjmyfTTw4/5SDEcN7gXWJmsSfzo50Yl32VJxuXA==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0yThh9uoOWQD5Go+3B4p\n6LRR8MOG/0fkMJrCYMbwK3TgLvIa/D/QnEtnLSa6CqwQlbL8QzCcLzqdxcux5QCf\nluwJChG2w87InAo6V/5roFc7BWei2sF68qQr3SGriNrHi7+DyYvkyeZfln/ukVFl\nA+EE2PoGMcP/2BsnW+9Z3mrDFgC+C57YOCLiNd1L1Fax9nq9FUuM7AbR3yCNkM/B\ntPDUrCJFoRkqLEbknVFIUjZyFjjL4NQh4yIJ8C73UcHl8bgTxZbzixU9evYyC1lx\n/RopnFnKpSz+I2LCHINUIcURDQYUi8b+zYpqLCJF8ZccLORofuswz6WZ1CfTzKXq\nBwIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "This is a secret message"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
