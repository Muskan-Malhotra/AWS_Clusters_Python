from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

users={
    'muskan2401':generate_password_hash('Pass@123456'),
    'siddhi100' : generate_password_hash('Pass#1234')
}


@auth.verify_password
def verify_password(username,password):

    if username in users:
        return check_password_hash(users.get(username),password),generate_password_hash(password)
    return False
    
