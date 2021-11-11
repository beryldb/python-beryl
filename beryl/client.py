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

from typing import List, Dict, Optional
from beryl.connection import SocketPool
from beryl.enums import Action, Connection, return_type, Command, all_commands, enabled_commands
from beryl.exceptions import ClientError
from beryl.protocol import Protocol
from beryl.parser import CheckFail, GetItem, GetVal2, GetVal, GetSimple, Handle, escape, QueryFailed, GetKeyVal

class Client:
    def __init__(
        self, host: str = 'localhost', port: int = 6378, login: str = 'root', password: str = 'default'
    ):
        self.host 	  =   host
        self.port 	  =   port
        self.login 	  =   login
        self.password     =   password
        self._connection  =   Connection.UNINITIALIZED
        self.pool 	  =   None  
        self.listing      =   0
        self.items        =   []
        self.maps         =   {}

    async def connection(self, connection: Connection) -> None:
        if self._connection != Connection.UNINITIALIZED:
            raise ClientError('Connection cannot be set twice')

        async def mock(*_, **__):
            raise ClientError(f'Command not available in {connection} connection')

        for command in all_commands:
            if command not in enabled_commands[connection]:
                setattr(self, command.value.lower(), mock)
        self._connection =  connection
        self.pool 	 =  SocketPool(
            host  	 =  self.host,
            port  	 =  self.port,
            login        =  self.login,
            password     =  self.password,
            connection   =  connection,
        )

    async def hget(self, map: str, hash: str) -> str:
        return GetVal(await self._command(Command.HGET, map, hash))

    async def get(self, key: str) -> str:
        return GetVal(await self._command(Command.GET, key))

    async def vsort(self, key: str) -> int:
        return GetSimple(await self._command(Command.VSORT, key))

    async def hlist(self, key: str) -> int:
        return await self._command(Command.HLIST, key)

    async def dblist(self) -> int:
        return await self._command(Command.DBLIST)

    async def coremodules(self, key: str = None) -> int:
        return await self._command(Command.COREMODULES, key=key)

    async def modules(self, key: str = None) -> int:
        return await self._command(Command.MODULES, key=key)

    async def listusers(self, key: str = None) -> int:
        return await self._command(Command.LISTUSERS, key=key)

    async def listadmins(self, key: str = None) -> int:
        return await self._command(Command.LISTADMINS, key=key)

    async def lsort(self, key: str) -> int:
        return GetSimple(await self._command(Command.LSORT, key))

    async def getdel(self, key: str) -> str:
        return GetVal(await self._command(Command.GETDEL, key))

    async def flushall(self) -> str:
        return GetSimple(await self._command(Command.FLUSHALL))

    async def flushdb(self) -> str:
        return GetSimple(await self._command(Command.FLUSHDB))

    async def pwd(self) -> str:
        return GetSimple(await self._command(Command.PWD))

    async def reset(self) -> str:
        return GetSimple(await self._command(Command.RESET))

    async def current(self) -> int:
        return GetSimple(await self._command(Command.CURRENT))

    async def version(self) -> int:
        return GetSimple(await self._command(Command.VERSION))

    async def exists(self, key: str) -> int:
        return GetSimple(await self._command(Command.EXISTS, key))

    async def dbsize(self, key: str = None) -> int:
        return GetSimple(await self._command(Command.DBSIZE, key=key))

    async def lcount(self, key: str) -> int:
        return GetSimple(await self._command(Command.LCOUNT, key))

    async def vcount(self, key: str) -> int:
        return GetSimple(await self._command(Command.VCOUNT, key))        
        
    async def hcount(self, key: str) -> int:
        return GetSimple(await self._command(Command.HCOUNT, key))
                
    async def vexists(self, key: str, hash: str) -> int:
        return GetSimple(await self._command(Command.VEXISTS, key, hash))

    async def lexists(self, key: str, hash: str) -> int:
        return GetSimple(await self._command(Command.LEXISTS, key, hash))
                
    async def hexists(self, key: str, hash: str) -> int:
        return GetSimple(await self._command(Command.HEXISTS, key, hash))

    async def db(self) -> int:
        return GetSimple(await self._command(Command.DB))

    async def lpopfront(self, key: str) -> str:
        return Handle(await self._command(Command.LPOPFRONT, key))

    async def vpopfront(self, key: str) -> str:
        return Handle(await self._command(Command.VPOPFRONT, key))

    async def vpopback(self, key: str) -> str:
        return Handle(await self._command(Command.VPOPBACK, key))

    async def change(self, key: str) -> str:
        return Handle(await self._command(Command.CHANGE, key))
    
    async def count(self, key: str) -> str:
        return GetSimple(await self._command(Command.COUNT, key))

    async def dbcreate(self, name: str, path: str = None) -> str:
        return Handle(await self._command(Command.DBCREATE, name, path=path))

    async def dbdelete(self, name: str) -> str:
        return Handle(await self._command(Command.DBDELETE, name))

    async def vresize(self, key: str, size: int) -> str:
        return GetSimple(await self._command(Command.VRESIZE, key, str(size)))

    async def lresize(self, key: str, size: int) -> str:
        return GetSimple(await self._command(Command.LRESIZE, key, str(size)))
        
    async def lpush(self, key: str, value: str) -> str:
        return Handle(await self._command(Command.LPUSH, key, escape(value)))

    async def rename(self, key: str, dest: str) -> str:
        return Handle(await self._command(Command.RENAME, key, dest))

    async def copy(self, key: str, dest: str) -> str:
        return Handle(await self._command(Command.COPY, key, dest))

    async def move(self, key: str, dest: str) -> str:
        return Handle(await self._command(Command.MOVE, key, dest))

    async def renamenx(self, key: str, dest: str) -> str:
        return Handle(await self._command(Command.RENAMENX, key, dest))

    async def vpush(self, key: str, value: str) -> str:
        return Handle(await self._command(Command.VPUSH, key, escape(value)))

    async def set(self, key: str, value: str) -> str:
        return Handle(await self._command(Command.SET, key, escape(value)))

    async def vpushnx(self, key: str, value: str) -> str:
        return Handle(await self._command(Command.VPUSHNX, key, escape(value)))

    async def expire(self, key: str, seconds: int) -> str:
        return Handle(await self._command(Command.EXPIRE, key, str(seconds)))

    async def setex(self, seconds: int, key: str, value: str) -> str:
        return GetSimple(await self._command(Command.SETEX, str(seconds), key, escape(value)))

    async def expireat(self, key: str, seconds: int) -> str:
        return Handle(await self._command(Command.EXPIREAT, key, str(seconds)))
        
    async def ttl(self, key: str) -> str:
        return GetSimple(await self._command(Command.TTL, key))

    async def strlen(self, key: str) -> str:
        return GetSimple(await self._command(Command.STRLEN, key))

    async def hstrlen(self, key: str, hash: str) -> str:
        return GetSimple(await self._command(Command.HSTRLEN, key, hash))

    async def vpos(self, key: str, pos: int) -> str:
        return GetVal(await self._command(Command.VPOS, key, str(pos)))

    async def lpos(self, key: str, pos: int) -> str:
        return GetVal(await self._command(Command.LPOS, key, str(pos)))

    async def rkey(self) -> str:
        return GetSimple(await self._command(Command.RKEY))

    async def ttlat(self, key: str) -> str:
        return GetSimple(await self._command(Command.TTLAT, key))

    async def isnum(self, key: str) -> str:
        return GetSimple(await self._command(Command.ISNUM, key))

    async def type(self, key: str) -> str:
        return GetSimple(await self._command(Command.TYPE, key))

    async def expires(self, key: str) -> str:
        return GetSimple(await self._command(Command.EXPIRES, key))

    async def restart(self) -> str:
        return GetSimple(await self._command(Command.RESTART))

    async def time(self) -> str:
        return GetVal2(await self._command(Command.TIME))

    async def epoch(self) -> str:
        return GetVal2(await self._command(Command.EPOCH))

    async def delete(self, key: str) -> str:
        return Handle(await self._command(Command.DEL, key))

    async def hset(self, key: str, hash: str, value: str) -> str:
        return Handle(await self._command(Command.HSET, key, hash, escape(value)))

    async def hdel(self, key: str, hash: str) -> str:
        return Handle(await self._command(Command.HDEL, key, hash))

    async def decr(self, key: str) -> str:
        return GetSimple(await self._command(Command.DECR, key))

    async def incr(self, key: str) -> str:
        return GetSimple(await self._command(Command.INCR, key))

    async def vlow(self, key: str) -> str:
        return GetSimple(await self._command(Command.VLOW, key))

    async def vhigh(self, key: str) -> str:
        return GetSimple(await self._command(Command.VHIGH, key))

    async def vavg(self, key: str) -> str:
        return GetSimple(await self._command(Command.VAVG, key))

    async def vfront(self, key: str) -> str:
        return GetVal(await self._command(Command.VFRONT, key))

    async def vback(self, key: str) -> str:
        return GetVal(await self._command(Command.VBACK, key))

    async def lback(self, key: str) -> str:
        return GetVal(await self._command(Command.LBACK, key))

    async def lfront(self, key: str) -> str:
        return GetVal(await self._command(Command.LFRONT, key))

    async def llow(self, key: str) -> str:
        return GetSimple(await self._command(Command.LLOW, key))

    async def lhigh(self, key: str) -> str:
        return GetSimple(await self._command(Command.LHIGH, key))

    async def loadmodule(self, key: str) -> str:
        return GetSimple(await self._command(Command.LOADMODULE, key))

    async def unloadmodule(self, key: str) -> str:
        return GetSimple(await self._command(Command.UNLOADMODULE, key))

    async def lavg(self, key: str) -> str:
        return GetSimple(await self._command(Command.LAVG, key))

    async def lget(self, key: str, offset: int = None, limit: int = None) -> str:
        return await self._command(Command.LGET, key, offset=offset, limit=limit)

    async def vget(self, key: str, offset: int = None, limit: int = None) -> str:
        return await self._command(Command.VGET, key, offset=offset, limit=limit)

    async def keys(self, key: str, offset: int = None, limit: int = None) -> str:
        return await self._command(Command.KEYS, key, offset=offset, limit=limit)

    async def lkeys(self, key: str, offset: int = None, limit: int = None) -> str:
        return await self._command(Command.LKEYS, key, offset=offset, limit=limit)

    async def vkeys(self, key: str, offset: int = None, limit: int = None) -> str:
        return await self._command(Command.VKEYS, key, offset=offset, limit=limit)

    async def quit(self) -> bytes:
        return await self._command(Command.QUIT)

    async def ldel(self, key: str, value: str) -> str:
        return Handle(await self._command(Command.LDEL, key, escape(value)))

    async def vdel(self, key: str, value: str) -> str:
        return Handle(await self._command(Command.VDEL, key, escape(value)))

    async def _command(self, command: Command, *args, **kwargs) -> bytes:
        if self._connection == Connection.UNINITIALIZED:
            raise ClientError('Call .connection before initializing')

        assert self.pool is not None
        c = await self.pool.get_connection()

        values = []
        for k in kwargs:
            if kwargs[k] is not None:
                if k == 'limit':
                    values.append(f'{kwargs[k]}')
                elif k == 'offset':
                    values.append(f'{kwargs[k]}')
                else:
                    values.append(kwargs[k])
        await c.write(f'{command.value} {" ".join(args)} {" ".join(values)}'.strip())
        result  = ""
        self.items = []
        self.maps  = {}
        
        parse_type = return_type(str(command))
        
        while True:
            result = await c.read()            
            tokens = result.split()
            parsed = int(tokens[1].decode("utf-8"))

            if parsed == Protocol.BRLD_PING:
                self.writer.write("PONG :1")
                continue
            elif parsed == Protocol.ERR_INPUT:
                await self.pool.release(c)
                raise QueryFailed(tokens[1].decode("utf-8"), tokens[3].decode("utf-8")[1:])
                continue
            elif parsed == Protocol.ERR_INPUT2:
                await self.pool.release(c)
                raise QueryFailed(tokens[1].decode("utf-8"), tokens[4].decode("utf-8")[1:])
                continue
                
            elif parsed == Protocol.BRLD_START_LIST:
                self.listing = 1
                continue
            elif parsed == Protocol.BRLD_END_LIST:
                await self.pool.release(c)
                self.listing = 0
                if parse_type == 0:
                    return self.items
                elif parse_type == 2:
                    return self.maps
                else:
                    return self.items
            elif parsed == Protocol.BRLD_ITEM_LIST:
                if parse_type == 0:
                    self.items.append(GetItem(result))
                elif parse_type == 2:	
                    key, val = GetKeyVal(result)
                    self.maps[key] = val
                else:
                    self.items.append(GetSimple(result))
                continue
            else:
                break;
            
        await self.pool.release(c)
        return result

