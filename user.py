from firebase_admin import auth,initialize_app,db,credentials
from firebase_admin._auth_utils import EmailAlreadyExistsError,UidAlreadyExistsError,UserNotFoundError
from email.message import EmailMessage
from smtplib import SMTP
from threading import Thread
from time import sleep
from requests import post


private_key_path = "utils\\private_key.json"
admin_mail = "seenusanjay20102002@gmail.com"
admin_password = "vdmzrapnlewbjrgm"

api_key = "AIzaSyAckgNM-WYs0ULGMF7WQ-HhIbfFLF51EBU" # web app
password_verification_link = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"  # google identity toolkit api



cred = credentials.Certificate(cert=private_key_path)
initialize_app(credential=cred,options = {"databaseURL":"https://repair-brain-20-default-rtdb.firebaseio.com"})



class User:

    def __init__(self,uid,email,password,name,last_name,verified=False):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.user_name = uid
        self.password = password
        self.verified = verified

        if name is not None and last_name is not None:
            self.full_name = name + " " +  last_name

        else:
            self.full_name = None


    def login_with_email(self,entered_password):
        try:
            json = {
                "email" : self.email,
                "password"  :entered_password
            }

            response = post(password_verification_link,json=json)
            json = response.json()

            #print(json)

            assert "error" not in json

            self.get_user_data(self.email,False)


        except AssertionError:
            msg = json["error"]["message"]

            #print(msg)

            if  msg == "INVALID_PASSWORD":
                return False,"Incorrect Password"
            
            elif msg == "EMAIL_NOT_FOUND":
                return False,"Email not Found"
            
            elif msg == "TOO_MANY_ATTEMPTS_TRY_LATER":
                return False,"Too many Attempts, Try Later"
            
            elif msg == "INVALID_EMAIL":
                return False,"Invalid E-mail ID"
            
            else:
                return False,"Something went wrong"
            
        except Exception as e:
            print(e,"Response")
            return False,"Something went Wrong"
        
        else:
            print("Login is successful")
            return True,"Login Successful"
        

    def login_with_uid(self,entered_password):
        try:
            user = auth.get_user(self.user_name)
            #print(user.email)
        
        except UserNotFoundError:
            return False,"User Not Found"
        
        except Exception as e:
            print(e,"login")
            return False,"Something went wrong"
        
        else:
            self.email = user.email 
            return self.login_with_email(entered_password)   
        

    def email_verified_using_id(self): 
        return self.email_verified
    

    def email_verified_using_email(email):
        user = auth.get_user_by_email(email)
        return user.email_verified
    

    def create_user_account(self):
        try:
            auth.create_user(display_name = self.full_name,uid=self.user_name,email=self.email,password=self.password,email_verified=False)
        
        except EmailAlreadyExistsError:
            return False,"Email already exists"
        
        except UidAlreadyExistsError:
            return False,"User name already exists"
        
        except:
            return False,"Something Went Wrong"
        
        else:
            return True,"Account Created"
        

    def get_username(self):
        return self.user_name
    

    def send_verification_link(self):
        verification_link = auth.generate_email_verification_link(self.email)
        msg = "Click on the link to verify your email : " + verification_link
        self.send_mail(msg)


    def send_password_reset_link(self):
        password_reset_link = auth.generate_password_reset_link(self.email)
        msg = "Click on the clink to reset the password : " + password_reset_link
        self.send_mail(msg)


    def is_user_verified(self):
        return self.verified
    

    def get_user_data(self,data,uid=True):
        if uid:
            user = auth.get_user(data)
        else:
            user = auth.get_user_by_email(data)

        self.email = user.email
        self.user_name = user.uid
        self.verified = user.email_verified
        self.full_name = user.display_name

        return self


    def send_mail(self,body,subject="Repair Brain"):
        smtp = SMTP(host="smtp.gmail.com",port=587)
        smtp.starttls()
        smtp.login(admin_mail,admin_password)

        email = EmailMessage()

        email["From"] = admin_mail
        email["To"] = self.email
        email["Subject"] = subject

        email.set_content(body)

        smtp.send_message(email)


    def get_data_base(self):
        return db.reference(self.user_name)
    

    @staticmethod
    def get_database_reference():
        return db.reference("/")


    def set_email_verified_listner(self):

        def thread():
            while True:
                user_data =  auth.get_user_by_email(self.email)
                verified = user_data.email_verified
                print(verified)
                if verified:
                    break

                sleep(5)

        thread = Thread(target=thread)
        thread.start()




# print(User.login_with_email("seenusanjay20102002@gmail.com","123456"))