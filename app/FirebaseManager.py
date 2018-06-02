
import firebase_admin
from firebase_admin import credentials, db

class FirebaseManager:

    def __init__(self):
        cred = credentials.Certificate('Files/Auth/smartmirror-75b89-firebase-adminsdk-vx8is-56d6e1cacc.json')
        #default_app = firebase_admin.initialize_app(cred)
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://smartmirror-75b89.firebaseio.com'
        })
        self.root = db.reference()
        self.weather = self.root.child('weather')
        self.image = self.root.child('image')


    def update_weather(self, weather_data):
        self.weather.update(weather_data)

    def get_weather(self):
        weather_data = db.reference('weather'.format(self.weather.key)).get()
        print(weather_data['cur_sky'], weather_data['cur_tem'], weather_data['max_tem'], weather_data['min_tem'])

    def update_image(self, uid, image_url):
        self.image.child(uid).update(image_url)

    def get_profile_name(self, uid):
        return self.image.child(uid).get()