import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flagships_data import flagships
from events_data import events

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def addCompleteData(collection_name="safety_collection"):
    '''
    Function to add whole collection into firestore
    '''

    list_data = []

    if collection_name == "Flagships":
        list_data = flagships

    elif collection_name == "Events":
        list_data = events

    else:
        list_data = []

    if len(list_data) == 0:
        print("Please check the collection name")

    else:
        for data in list_data:
            db.collection(collection_name).add(data)

        print("Write Complete.")


def addNewTechnitude(collection_name="safety_collection"):
    '''
    Function to add new event intp firebase collection, append a new disctionary in the data file.
    '''

    db.collection(collection_name).add(events[-1])

    print("Write Complete.")


def readCompleteData(collection_name="safety_collection"):
    '''
    Function to read whole collection from firestore
    '''

    result = db.collection(collection_name).stream()

    for doc in result:
        print(f'{doc.id} => {doc.to_dict()}', end="\n\n")

    print(result)

    print("Read Complete. If you did not get what you wanted, please check the collection name.")
