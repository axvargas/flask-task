import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials, {
    'projectId': 'platzi-flask-326306'
    })


db = firestore.client()

def get_users():
    return db.collection(u'users').get()

def get_user(user_id):
    return db.collection(u'users').document(user_id).get()

def get_todos(user_id):
    return db.collection(u'users').document(user_id).collection(u'todos').get()

def create_user(user_data):
    doc_ref = db.collection(u'users').document(user_data.username)
    doc_ref.set({'password': user_data.password})

def create_todo(user_id, todo_data):
    doc_ref = db.collection(u'users').document(user_id).collection(u'todos').document()
    doc_ref.set(todo_data)

def delete_todo(user_id, todo_id):
    doc_ref = db.collection(u'users').document(user_id).collection(u'todos').document(todo_id)
    doc_ref.delete()

def update_todo(user_id, todo_id, todo_data):
    doc_ref = db.collection(u'users').document(user_id).collection(u'todos').document(todo_id)
    doc_ref.update(todo_data)