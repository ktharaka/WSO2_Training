import sys
import hashlib

text = str.encode(sys.argv[1]);
hash = hashlib.pbkdf2_hmac('sha512', text, b'Km5d5ivMy8iexuHcZrsD', 200000);
print(hash.hex());
