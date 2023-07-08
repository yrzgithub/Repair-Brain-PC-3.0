from pyrebase import initialize_app
from requests.exceptions import HTTPError
from email.message import EmailMessage
from smtplib import SMTP
from threading import Thread
from json import loads



config = {

  "apiKey": "AIzaSyAckgNM-WYs0ULGMF7WQ-HhIbfFLF51EBU",
  "authDomain": "repair-brain-20.firebaseapp.com",
  "databaseURL": "https://repair-brain-20-default-rtdb.firebaseio.com",
  "projectId": "repair-brain-20",
  "storageBucket": "repair-brain-20.appspot.com",
  "messagingSenderId": "935756194550",
  "appId": "1:935756194550:web:20b9ded256fa2198d242d7",
  "measurementId": "G-CSQLLQMDXL"

}

app = initialize_app(config=config)
db = app.database()
auth = app.auth()



class User:

    def __init__(self,username,email,password,name,last_name,verified=False):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.user_name = username
        self.password = password
        self.verified = verified

        if name is not None and last_name is not None:
            self.full_name = name + " " +  last_name

        else:
            self.full_name = None


    def login_with_email(self,entered_password):                                                  # done
        try:
            results = auth.sign_in_with_email_and_password(self.email,password=entered_password)
            print(results)
            
        except HTTPError as e:
            json_error = loads(e.strerror)
            error = json_error["error"]["message"].lower().replace("_"," ").title()
            return False,error
            
        except Exception as e:
            #print(e)
            return False,"Something went Wrong"

        else:
            print("Login is successful")
            self.idToken = results["idToken"]
            self.get_user_data()
            return True,"Login Successful"
        

    def login_with_username(self,entered_password):                                                   # done
        email_data = db.child("ids").get().val()

        if email_data is None:
            return False,"Username Not Found"
        
        email = email_data[self.user_name]
        self.email = email
        return self.login_with_email(entered_password)
    

    def create_user_account(self):                                                                       # done
        try:
            results = auth.create_user_with_email_and_password(email=self.email,password=self.password)
            print(results)

        except HTTPError as e:
            error_json = loads(e.strerror)
            print(error_json)

            message = error_json["error"]["message"].lower().replace("_"," ").title()

            return False,message
            
        except:
            return False,"Something Went Wrong"
        
        else:
            append = {self.user_name:self.email}
            db.child("ids").update(append)

            self.idToken = results["idToken"]
            idToken = self.idToken
            auth.update_profile(id_token=idToken,display_name=self.full_name)
            
            return True,"Account Created"
        

    def send_verification_link(self):
        (success,msg) = self.login_with_email(self.password)
        if success:
            auth.send_email_verification(self.idToken)
        return (success,msg)


    @staticmethod
    def send_password_reset_link(email):
        try:
            error_json = auth.send_password_reset_email(email)
        
        except HTTPError as e:
            error_json = loads(e.strerror)
            message = error_json["error"]["message"].lower().replace("_"," ").title()
            return False,message

        except:
            return False,"Something Went Wrong"

        else:
            return True,"Password Resent Link Sent"
        

    def is_user_verified(self):
        return self.verified
    

    def get_user_data(self):
        user = auth.get_account_info(self.idToken)
        data = user["users"][0]
        self.email = data["email"] 
        self.verified = data["emailVerified"]

        return self
    

    def get_data_base(self):
        return db.reference(self.user_name)
    

    @staticmethod
    def get_database_reference():
        return db



# a = User("uruttu",None,"#Jaihind",None,None)
# a.login_with_username("#Jaihind") #login_with_email("#Jaihind")
 #print(a.get_user_data())

# print(User.send_password_reset_link("123"))