#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
with app.app_context():
    db.create_all()


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
