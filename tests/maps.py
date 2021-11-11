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
  await link.flushall()
  
  # Creates map 'a' with hash 'b' and value 'c'. 
    
  try:
     print (await link.hset("a", "b", "c"))
  except Exception as error:     
     print(error.message)
  
  # Retrieves map 'a' and hash b
  
  try:
     print (await link.hget("a", "b"))
  except Exception as error:     
     print(error.message)
     
  # List all items associated with list 'a'
  
  try:
     for key in (await link.hlist("a")):
        print(key)
  except Exception as error:
     print(error.message)

  # We remove hash b from map 'a'
  
  try:
     print (await link.hdel("a", "b"))
  except Exception as error:     
     print(error.message)
     
if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())