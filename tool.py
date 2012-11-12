#!/usr/bin/python
import hashlib
email = raw_input('Email address? ')
salt = '#ioe12'
hash = hashlib.sha256(email + salt)
print (salt.encode('hex'), hash.hexdigest())
