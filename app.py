from fastfix.configuration.config import app, sql
from fastfix.controller import UserController, StackOverFlowController, PasswordMagicLinkController, \
    ResearchController

sql.create_all()

# controllers init
app.register_blueprint(PasswordMagicLinkController.passwordMagicLink)
app.register_blueprint(ResearchController.research)
app.register_blueprint(StackOverFlowController.stackOverFlow)
app.register_blueprint(UserController.user)