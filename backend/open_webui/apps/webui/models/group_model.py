# models/group_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..internal.db import db
from peewee import Model, CharField

class Group(Model):
    name = CharField(unique=True)

    class Meta:
        database = db
        table_name = 'groups'

