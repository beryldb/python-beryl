# python-beryl - Python Driver for BerylDB.
# http://www.beryldb.com
#
# This is an example script for python-beryl. You may modify it
# and freely use it at your convenience. Feel free to join our
# discord support server If you are interested about BerylDB.

import asyncio
import sys
sys.path.insert(0,'..')

from beryl import Client
from beryl.enums import Connection

async def main():
  link = Client(host='127.0.0.1', port=6378, login='root', password='default')
  await link.connection(Connection.Server)
  
  # FlushDB
    
  try:
     print (await link.flushdb())
  except Exception as error:     
     print(error.message)
     
  # FlushAll
    
  try:
     print (await link.flushall())
  except Exception as error:     
     print(error.message)

  # List all modules

  try:
     mods = (await link.modules())
     for key, value in mods.items():
        print(key, '->', value)
  except Exception as error:
     print(error.message)

  # List all coremodules

  try:
     mods = (await link.coremodules())
     for key, value in mods.items():
        print(key, '->', value)
  except Exception as error:
     print(error.message)
     
  # List all databases 
  
  try:
     mods = (await link.dblist())
     for key, value in mods.items():
        print(key, '->', value)
  except Exception as error:
     print(error.message)
    
  # Current working directory

  try:
     print (await link.pwd())
  except Exception as error:
     print(error.message)

  # Load a module

  try:
     print (await link.loadmodule("forcejoin"))
  except Exception as error:
     print(error.message)
 

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())