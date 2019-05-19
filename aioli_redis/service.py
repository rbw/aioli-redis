# -*- coding: utf-8 -*-

import asyncio_redis

from aioli.package.service import BaseService


class RedisService(BaseService):
    async def get_connection(self):
        return await asyncio_redis.Connection.create(
            host='127.0.0.1',
            port=6379,
            loop=self.loop
        )

    async def subscribe(self, channel):
        connection = await self.get_connection()
        subscription = await connection.start_subscribe()

        await subscription.subscribe([channel])

        return connection, subscription

