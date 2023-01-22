from flask import Blueprint, request
from flask_cors import cross_origin
from fastanswers.model.repository.UserRepository import UserRepository
from fastanswers.service.UserService import UserService
from fastanswers.utils.Util import Util

user: Blueprint = Blueprint('UserController', __name__, url_prefix=Util.getURL('user'))

userRepository: UserRepository = UserRepository()
userService: UserService = UserService(userRepository)


@user.route("/signin", methods=['POST'])
@cross_origin()
def signin():
    return userService.signin(request.json)


@user.route("/signup", methods=['POST'])
@cross_origin()
def signup():
    return userService.signup(request.json)




