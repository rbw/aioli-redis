# -*- coding: utf-8 -*-

from aioli import Package
from .service import RedisService
from .database import RedisModel

__version__ = '0.1.0'

export = Package(
    name='aioli-redis',
    description='Aioli Redis Service and Management API',
    controllers=[],
    services=[RedisService],
    models=[RedisModel],
)
