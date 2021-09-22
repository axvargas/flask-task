'''
Created Date: Thursday September 16th 2021 10:17:16 pm
Author: Andrés X. Vargas
-----
Last Modified: Thursday September 16th 2021 10:42:34 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views