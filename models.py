from peewee import *
import peewee


database = SqliteDatabase('flask_test.db')
class BaseModel(Model):
    class Meta:
        database = database


class users(BaseModel):
    user_id = IntegerField(primary_key=True)
    user_name = CharField(unique=True)
    user_password = CharField(null=True)
    user_status =  CharField(default='offline')

    def __unicode__(self):
        return self.user_name
