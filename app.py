from fastanswers.configuration.config import app, sql
from fastanswers.controller import UserController, StackOverFlowController

sql.create_all()

# controllers init
app.register_blueprint(StackOverFlowController.stackOverFlow)
app.register_blueprint(UserController.user)