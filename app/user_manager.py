import hashlib


ACCOUNT_DETAILS_FILEPATH = "data/users.txt"


def save_user(email, hashed_pwd):
    # save to file
    with open(ACCOUNT_DETAILS_FILEPATH, "a") as f:
        f.write(f"{email} {hashed_pwd}\n")


def existing_user(email):

    with open(ACCOUNT_DETAILS_FILEPATH, "r") as f:
        for line in f:
            components = line.split()
            if components[0] == email:
                return True
    return False


def authenticate_user(username, password):

    with open(ACCOUNT_DETAILS_FILEPATH, "r") as f:
        for line in f:
            components = line.split()
            print("part", components)
            if components[0] == username:
                hashed_password = components[1]
                if hashed_password == hash_password(password):
                    return True
                else:
                    return False
    return False


def hash_password(pwd):
    # hash a password using SHA-256 algorithm
    pwd_bytes = pwd.encode('utf-8')
    hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
    return hashed_pwd

