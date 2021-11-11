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
  
  # Sets key 'hello' and assigns value world.
    
  try:
     print (await link.set("hello", "world"))
  except Exception as error:     
     print(error.message)

  # Sets a timeout on key 'hello
  
  try:
     print (await link.expire("hello", 300))
  except Exception as error:     
     print(error.message)

  # Checks if given key expires
  
  try:
     print (await link.expires("hello"))
  except Exception as error:
     print(error.message)

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())