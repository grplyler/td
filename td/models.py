from peewee import *
from datetime import datetime
import os

# Setup CONF
DATA_ROOT = os.path.expanduser('~/.td/')
CONF_FILE = os.path.join(DATA_ROOT, 'conf.yml')
DB_FILE = os.path.join(DATA_ROOT, 'todos.db')


db = SqliteDatabase(DB_FILE)


class Project(Model):

    name = CharField()
    date_created = DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'projects'

class Todo(Model):

    project = CharField()
    content = CharField()
    date_created = DateTimeField(default=datetime.now())
    date_finished = DateTimeField(null=True)
    status = CharField()
    visible = BooleanField(default=True)

    class Meta:
        database = db
        db_tables = 'todos'


def init_db():
    db.connect()
    db.create_tables([Project, Todo])

    # Add default project
    dpro = Project(name="default", date_created=datetime.now())
    dpro.save()
