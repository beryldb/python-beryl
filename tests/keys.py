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
  
  # We set key 'hello' and assign value world
    
  try:
     print (await link.set("hello", "world"))
  except Exception as error:     
     print(error.message)

  # Let's retrieve key 'hello'
  
  try:
     print (await link.get("hello"))
  except Exception as error:     
     print(error.message)

  # Let's obtain length of key 'hello' 
  
  try:
     print (await link.strlen("hello"))
  except Exception as error:     
     print(error.message)

  # List all keys
  
  try:
     for key in (await link.keys("*")):
        print(key)
  except Exception as error:     
     print(error.message)
  

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())