import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from events_data import events

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

result = db.collection(u'Events').stream()


print(events)