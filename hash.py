import hashlib

def hash_creds(email, password):
    creds = email + password
    hashed = hashlib.sha256(creds.encode('UTF-8'))
    return hashed.hexdigest()
