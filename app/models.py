'''
Created Date: Friday September 17th 2021 11:35:23 pm
Author: Andrés X. Vargas
-----
Last Modified: Tuesday September 21st 2021 9:38:53 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from flask_login import UserMixin
from .firestore_service import get_user
class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin):
    def __init__(self, user_data):
        """[summary]

        Args:
            user_data (UserData): Data of the user
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dict()['password']
        )
        return UserModel(user_data)