from fastfix.configuration.config import sql
from fastfix.model.entity.Research import Research
from fastfix.model.entity.User import User
from fastfix.utils.Util import Util


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 23/01/23
# Created at: 15:04
# Version: 1.0.0
# Description: This is the class for the research repository
#

class ResearchRepository():

    def __init__(self):
        pass

    def add(self, name, userId):
        research: Research = Research(name, userId)
        sql.session.add(research)
        sql.session.commit()

    def get(self, userId):
        researches: list = sql.session.query(Research).filter(Research.userId == userId).all()
        return researches
