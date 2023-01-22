from fastanswers.configuration.config import sql
from fastanswers.model.entity.PasswordMagicLink import PasswordMagicLink
from fastanswers.utils.Util import Util


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class PasswordMagicLinkRepository():

    def __init__(self):
        pass

    def create(self, userId):
        passwordMagicLink: PasswordMagicLink = PasswordMagicLink(Util.createLink(), userId)
        sql.session.add(passwordMagicLink)
        sql.session.commit()