from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
import pyrebase

firebaseConfig ={ 'apiKey': "AIzaSyBuDf7ZgH9YXdmdv-GBNMVnRqxcXU8usx4",
    'authDomain': "finaldb-3d671.firebaseapp.com",
    'databaseURL':"",
    'projectId': "finaldb-3d671",
    'storageBucket': "finaldb-3d671.appspot.com",
    'messagingSenderId': "758989072310",
    'appId': "1:758989072310:web:4b47799472a600d4594317",
    'measurementId': "G-KEGQGBHDG5"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


Window.size = (380, 600)

def invalidLogin():
    dialog = MDDialog(
        title="Invalid e-mail or password",
        text="Please try again"

    )
    dialog.width = "250"
    dialog.open()

def validSignup():
    dialog = MDDialog(
        title="You have successfully signed up",
        text="You can go back to the log in page to start using the app"

    )
    dialog.width = "250"
    dialog.open()

def invalidSignup():
    dialog = MDDialog(
        title="Invalid  email or password",
        text = "The password has to contain at least 6 characters"

    )
    dialog.width = "250"
    dialog.open()


class MyProfile(Screen):
    pass
class PostPage(Screen):
    pass
class LogInPage(Screen):
    email1 = ObjectProperty(None)
    password1 = ObjectProperty(None)

    def verify_login(self):
        try:
            auth.sign_in_with_email_and_password(self.email1.text,self.password1.text)
            return True
        except:
            invalidLogin()



class SignUpPage(Screen):
    email2 = ObjectProperty(None)
    password2 = ObjectProperty(None)

    def check_signup(self):
        if self.email2.text != "" and self.email2.text.count("@") == 1:
            if len(self.password2.text) > 5:
                try:
                    auth.create_user_with_email_and_password(self.email2.text, self.password2.text)
                    validSignup()
                except:
                    invalidSignup()

            else:
                invalidSignup()
        else:
            invalidSignup()


class MainPage(Screen):
    pass
class AddPost(Screen):
    pass
class UserProfile(Screen):
    pass


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_manager()

    def create_manager(self):
        LOGIN = LogInPage(name="login")
        SIGNUP = SignUpPage(name="signup")
        MAINPAGE = MainPage(name="mainpage")
        POSTPAGE = PostPage(name="postpage")
        MYPROFILE = MyProfile(name="myprofile")
        ADDPOST = AddPost(name="addpost")
        USERPROFILE = UserProfile(name="userprofile")
        self.add_widget(LOGIN)
        self.add_widget(SIGNUP)
        self.add_widget(MAINPAGE)
        self.add_widget(POSTPAGE)
        self.add_widget(MYPROFILE)
        self.add_widget(ADDPOST)
        self.add_widget(USERPROFILE)
        self.current = "login"


class FinalMain(MDApp):
    def __init__(self, **kwargs):
        self.title = "ArchBit"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    def build(self):
        Builder.load_file("FinalMain1.kv")
        return Manager()

if __name__ == '__main__':
    FinalMain().run()
