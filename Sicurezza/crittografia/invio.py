from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

pDest="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1860g4EdDj175BImYOe1\nZPLhBr5KfNbvW6xyJQGfGaOHB6hkmEpIWXquibfZ9PGyr9gDe/9xAeqD1A93RceK\nUL7poHBOLjtRypgysokeJkRnYAsbWa2pTQ9GaxGxHQClZ3RDnvA32J8J5e9224Vk\nL/bZKn7ohd0qnXBxVg67lUMUvP9wOVOyp4pq8vHMUaKO118ANrPDW4V+x6AKKY/J\nBCw0L+BRb6T52hUmCGzA6OVYUiCrbqi7h6z7i+Drc0Peg1csU2s2LChNeb/3qFyd\nDsaH36fzWT2lMHdyIbdKLUuAZQvYcj5Q8FnMLsz+8D8UUxA42DDqlBpWWiUmls/L\ndQIDAQAB\n-----END PUBLIC KEY-----"
public_key = RSA.import_key(pDest)

def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")

message = input("Messaggio da inviare:\n")
encrypted_message = encrypt_message(message, public_key)
print("Encrypted Message:", encrypted_message)
