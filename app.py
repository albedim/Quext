from quext.configuration.config import app, sql
from quext.controller import UserController, PasswordMagicLinkController, SummaryController

# controllers init
app.register_blueprint(PasswordMagicLinkController.passwordMagicLink)
app.register_blueprint(SummaryController.summary)
app.register_blueprint(UserController.user)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run(host="192.168.1.10")