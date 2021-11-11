# 
# python-beryl - Python Driver for BerylDB.
# http://www.beryldb.com
#
# This is an example script for python-beryl. You may modify it
# and freely use it at your convenience. Feel free to join our
# discord support server If you are interested about
# BerylDB. 
#

import asyncio

from beryl import Client
from beryl.enums import Connection

async def main():
  link = Client(host='127.0.0.1', port=6378, login='root', password='default')
  await link.connection(Connection.Server)

  # Let's remove all data
  
  await link.flushall()
  
  # We set a key 'hello' 
  
  try:
     print (await link.set("hello", "world"))
  except Exception as error:     
     print(error.message)

  # We set a map 'a' with hash 'b' and value 'c'. 

  try:
     print (await link.hset("a", "b", "c"))
  except Exception as error:     
     print(error.message)

  # We create list 'd' and push item 'f'

  try:
     print (await link.lpush("d", "f"))
  except Exception as error:     
     print(error.message)

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())