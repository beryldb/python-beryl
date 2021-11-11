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

from enum import Enum
from itertools import chain

from typing import Set

class Action(Enum):
    CONSOLIDATE = 'consolidate'
    BACKUP = 'backup'
    RESTORE = 'restore'

class Command(Enum):
    GET       = 'GET'
    INCR      = 'INCR'
    VGET      = 'VGET'
    CHANGE    = 'CHANGE'
    LBACK     = 'LBACK'
    LFRONT    = 'LFRONT'
    DECR      = 'DECR'
    HDEL      = 'HDEL'
    VEXISTS   = 'VEXISTS'
    LEXISTS   = 'LEXISTS'
    GETDEL    = 'GETDEL'
    LKEYS     = 'LKEYS'
    VKEYS     = 'VKEYS'
    DEL	      = 'DEL'
    VPOPBACK  = 'VPOPBACK'
    LRESIZE   = 'LRESIZE'
    EXPIRE    = 'EXPIRE'
    EXPIREAT  = 'EXPIREAT'
    HGET      = 'HGET'
    LPUSH     = 'LPUSH'
    VPUSH     = 'VPUSH'
    TYPE      = 'TYPE'
    VPUSHNX   = 'VPUSHNX'
    DBLIST    = 'DBLIST'
    VHIGH     = 'VHIGH'
    VLOW      = 'VLOW'
    VAVG      = 'VAVG'
    VBACK     = 'VBACK'
    LISTUSERS = 'LISTUSERS'
    LISTADMINS = 'LISTADMINS'
    VFRONT    = 'VFRONT'
    LGET      = 'LGET'
    TTLAT     = 'TTLAT'
    RESET     = 'RESET'
    ISNUM     = 'ISNUM'
    STRLEN    = 'STRLEN'
    SETEX     = 'SETEX'
    HSTRLEN   = 'HSTRLEN'
    DBCREATE  = 'DBCREATE'
    DBDELETE  = 'DBDELETE'
    HLIST     = 'HLIST'
    MODULES   = 'MODULES'
    RENAME    = 'RENAME'
    LHIGH     = 'LHIGH'
    LLOW      = 'LLOW'
    RENAMENX  = 'RENAMENX'
    HCOUNT    = 'HCOUNT'
    LCOUNT    = 'LCOUNT'
    VCOUNT    = 'VCOUNT'
    VRESIZE   = 'VRESIZE'
    COREMODULES   = 'COREMODULES'
    LDEL      = 'LDEL'
    VDEL      = 'VDEL'
    RKEY      = 'RKEY'
    LOADMODULE = 'LOADMODULE'
    UNLOADMODULE = 'UNLOADMODULE'
    LPOPFRONT = 'LPOPFRONT'
    VPOPFRONT = 'VPOPFRONT'
    TIME      = 'TIME'
    EPOCH     = 'EPOCH'
    EXPIRES   = 'EXPIRES'
    LPOS      = 'LPOS'
    DBSIZE    = 'DBSIZE'
    VERSION   = 'VERSION'
    VPOS      = 'VPOS'
    FLUSHALL  = 'FLUSHALL'
    FLUSHDB   = 'FLUSHDB'
    COUNT     = 'COUNT'
    LSORT     = 'LSORT'
    VSORT     = 'VSORT'
    KEYS      = 'KEYS'
    PWD	      = 'PWD'
    COPY      = 'COPY'
    MOVE      = 'MOVE'
    LAVG      = 'LAVG'
    TTL	      = 'TTL'
    HEXISTS   = 'HEXISTS'
    CURRENT   = 'CURRENT'
    EXISTS    = 'EXISTS'
    HSET      = 'HSET'
    QUIT      = 'QUIT'
    RESTART   = 'RESTART'
    DB	      = 'DB'
    SET       = 'SET'
    FLUSHB    = 'FLUSHB'

class Connection(Enum):
    UNINITIALIZED = 'uninitialized'
    Server 	= 'server'

currency_dict = { 'Command.LISTUSERS' : 2, 'Command.LISTADMINS' : 2, 'Command.DBLIST' : 2, 'Command.MODULES' : 2, 'Command.COREMODULES' : 2, 'Command.HLIST': 1, 'Command.KEYS'  : 1, 'Command.LKEYS' : 1, 'Command.VKEYS' : 1 }

def return_type(val):
    if not currency_dict.get(val):
        return 0
    else:
        return currency_dict[val]
        
enabled_commands = {
    Connection.UNINITIALIZED: 
    {
        Command.QUIT,
    },
    
    Connection.Server: 
    {
        Command.GET,
        Command.DBLIST,
        Command.RESET,
        Command.HLIST,
        Command.LISTUSERS,
        Command.LISTADMINS,
        Command.SETEX,
        Command.DEL,
        Command.DBSIZE,
        Command.VERSION,
        Command.VPUSHNX,
        Command.LEXISTS,
        Command.VEXISTS,
        Command.COREMODULES,
        Command.FLUSHALL,
        Command.FLUSHDB,
        Command.LSORT,
        Command.VSORT,
        Command.LCOUNT,
        Command.HDEL,
        Command.EXPIRES,
        Command.DECR,
        Command.MODULES,
        Command.LDEL,
        Command.VDEL,
        Command.CHANGE,
        Command.LKEYS,
        Command.LOADMODULE,
        Command.UNLOADMODULE,
        Command.LPOS,
        Command.VPOS,
        Command.VKEYS,
        Command.VFRONT,
        Command.LBACK,
        Command.LFRONT,
        Command.COUNT,
        Command.DBDELETE,
        Command.DB,
        Command.VCOUNT,
        Command.LBACK,
        Command.VBACK,
        Command.COPY,
        Command.MOVE,
        Command.HSTRLEN,
        Command.VRESIZE,
        Command.RESTART,
        Command.VPOPBACK,
        Command.RENAME,
        Command.RKEY,
        Command.DBCREATE,
        Command.RENAMENX,
        Command.TTLAT,
        Command.INCR,
        Command.VGET,
        Command.LHIGH,
        Command.LLOW,
        Command.LAVG,
        Command.VAVG,
        Command.VLOW,
        Command.VHIGH,
        Command.KEYS,
        Command.STRLEN,
        Command.EXPIREAT,
        Command.EXISTS,
        Command.EXPIRE,
        Command.TTL,
        Command.TYPE,
        Command.LRESIZE,
        Command.TIME,
        Command.EPOCH,
        Command.PWD,
        Command.HCOUNT,
        Command.ISNUM,
        Command.LGET,
        Command.GETDEL,
        Command.LPUSH,
        Command.HEXISTS,
        Command.HGET,
        Command.HSET,
        Command.VPUSH,
        Command.QUIT,
        Command.SET,
    },
}

all_commands = set(chain(*enabled_commands.values()))  
