from fastanswers.configuration.config import sql
from fastanswers.model.entity.User import User
from fastanswers.utils.Util import Util


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class UserRepository():

    def __init__(self):
        pass

    def signin(self, email, password) -> User:
        user: User = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    def signup(self, name, email, password) -> None:
        user: User = User(name, email, password)
        sql.session.add(user)
        sql.session.commit()

    def exists(self, email):
        users: User = sql.session.query(User).filter(User.email == email).count()
        return users

    def changePassword(self, userId, password):
        user: User = sql.session.query(User).filter(User.userId == userId).first()
        user.password = password
        sql.session.commit()
