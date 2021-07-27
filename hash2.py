import sys
import hashlib
import string
import secrets

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(20))
salt = str.encode(password);
text = str.encode(sys.argv[1]);
hash = hashlib.pbkdf2_hmac('sha512', text, salt, 200000);
print(hash.hex());
