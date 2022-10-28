from passlib.context import CryptContext

# Hashing the password 
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated= "auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)