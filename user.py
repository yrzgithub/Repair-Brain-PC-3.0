from firebase_admin import auth,initialize_app,db,credentials
from firebase_admin._auth_utils import UserNotFoundError,EmailAlreadyExistsError,UidAlreadyExistsError



private_key_path = "utils\\private_key.json"
cred = credentials.Certificate(cert=private_key_path)
initialize_app(credential=cred,options = {"databaseURL":"https://repair-brain-20-default-rtdb.firebaseio.com"})


def get_database():
    return db.reference("/")



class User:

    user_name = None
    name = None
    email = None 
    password = None
    verified = False

    def __init__(self,uid,email,name,password,verified=False):
        self.name = name
        self.email = email
        self.user_name = uid
        self.password = password
        self.verified = verified


    def create_user(self):
        if not self.check_if_user_exists():
            auth.create_user(display_name = self.name,uid=self.user_name,email=self.email,password=self.password,email_verified=False)
            print("New user Created")
            return True
    

    def check_if_user_exists(self):
        try:
            auth.get_user(self.user_name)
            return True
        
        except EmailAlreadyExistsError:
            print("Email already exists")
            return False 
        
        except UidAlreadyExistsError:
            print("User name already exists")
            return False
            

    def verify(self):
        if not self.verified:
            auth.generate_email_verification_link(self.email)
        print("Email Already Verified")


    def is_user_verified(self):
        return self.verified
    

    def get_user_data(self,uid):
        user = auth.get_user(uid)
        self.email = user.email
        self.password = user.password
        self.name = user.name
        self.verified = user.email_verified


    def reset_pasword(self):
        auth.generate_password_reset_link(self.email)