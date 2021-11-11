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
  
  # Inserts item into 'vector1'
    
  try:
     print (await link.vpush("vector1", "item"))
  except Exception as error:     
     print(error.message)

  # Returns all items on vector 'vector1'

  try:
     for item in (await link.vget("vector1")):
        print(item)
  except Exception as error:
     print(error.message)

  # Returns all vectors

  try:
     for item in (await link.vkeys("*")):
        print(item)
  except Exception as error:
     print(error.message)

  # Returns last item from 'vector1'
    
  try:
     print (await link.vback("vector1"))
  except Exception as error:     
     print(error.message)

  # Counts items on 'vector1'
    
  try:
     print (await link.vcount("vector1"))
  except Exception as error:     
     print(error.message)

  # Resizes 'vector1' to 1
    
  try:
     print (await link.vresize("vector1", 1))
  except Exception as error:     
     print(error.message)

  # Deletes item from 'vector1'
    
  try:
     print (await link.ldel("vector1", "item"))
  except Exception as error:     
     print(error.message)


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())