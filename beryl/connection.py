# BerylDB - A modular database.
# http://www.beryldb.com
#
# Copyright (C) 2021 Carlos F. Ferry <cferry@beryldb.com>
# 
# This file is part of BerylDB. BerylDB is free software: you can
# redistribute it and/or modify it under the terms of the BSD License
# version 3.
#
# More information about our licensing can be found at https://docs.beryl.dev

import asyncio
from logging import getLogger

from typing import Set, Optional

from beryl.enums import Connection
from beryl.exceptions import ServerError, ConnectionClosed
from beryl.protocol import Protocol

class Connection:
    def __init__(self, host: str, port: int, login: str, password: str):
        self.host 	= 	host
        self.port 	= 	port
        self.login 	= 	login
        self.password   = 	password
        self.reader 	= 	None  
        self.writer 	= 	None  
        self.logger 	= 	getLogger('connection')
        
    async def connect(self) -> None:

        try:
            self.reader, self.writer = (await asyncio.open_connection(self.host, self.port))
        except Exception as e:
            print("Unable to connect to: " + self.host + ':' + str(self.port))
            exit()

        await self.write(f'ILOGIN python1 ' + str(self.password) + ' ' + str(self.login))
        result = await self.read()
        tokens = result.split()
        parsed = int(tokens[1].decode("utf-8"))
        
        if parsed == Protocol.ERR_WRONG_PASS:
            print ("Incorrect password.")
            exit()
        elif parsed == Protocol.ERR_INPUT:
            print ("Incorrect login.")
            exit()
        elif parsed == Protocol.BRLD_CONNECTED:
           #print ("Connected!")
           self.me = tokens[2].decode("utf-8")

    async def write(self, msg: str) -> None:
        assert self.writer is not None, 'connect'
        self.writer.write(((msg + '\r\n').encode()))
        await self.writer.drain()

    async def read(self) -> bytes:
        assert self.reader is not None
        line = (await self.reader.readline()).strip()
        tokens = line.split()
        parsed = int(tokens[1].decode("utf-8"))
        return line

class SocketPool:
    def __init__(self, host: str, port: int, connection: Connection, login: str, password: str, max_connections: int = 100):
        self.closed 			= 	False
        self._created_connections 	= 	0
        self._available_connections     = 	asyncio.Queue()  
        self._in_use_connections        = 	set()  
        self.max_connections            = 	max_connections
        self.host 			= 	host
        self.port 			= 	port
        self.login 			= 	login
        self.password 			= 	password
        self.connection 		= 	connection
        
    async def get_connection(self) -> Connection:
        if self.closed is True:
            raise ConnectionClosed('Connection pool is closed')
        try:
            connection = self._available_connections.get_nowait()
        except asyncio.QueueEmpty:
            connection = await self.make_connection()
        self._in_use_connections.add(connection)
        return connection

    async def make_connection(self) -> Connection:
        if self._created_connections >= self.max_connections:
            return await self._available_connections.get()
        self._created_connections += 1
        con = Connection(self.host, self.port, self.login, self.password)
        await con.connect()
        return con

    async def release(self, connection: Connection) -> None:
        self._in_use_connections.remove(connection)
        await self._available_connections.put(connection)

    async def destroy(self):
        self.closed = True
