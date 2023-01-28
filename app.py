from quext.configuration.config import app, sql
from quext.controller import UserController, PasswordMagicLinkController, SummaryController

sql.create_all()

# controllers init
app.register_blueprint(PasswordMagicLinkController.passwordMagicLink)
app.register_blueprint(SummaryController.summary)
app.register_blueprint(UserController.user)