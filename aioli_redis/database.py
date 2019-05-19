# -*- coding: utf-8 -*-

import datetime
import orm

from aioli.db import Model


class RedisModel(Model):
    __tablename__ = 'package_mapping'

    id = orm.Integer(primary_key=True)
    db = orm.Integer(unique=True)
    package_name = orm.String(unique=True, max_length=128)
