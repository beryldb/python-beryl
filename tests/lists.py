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
import sys
sys.path.insert(0,'..')

from beryl import Client
from beryl.enums import Connection

async def main():
  link = Client(host='127.0.0.1', port=6378, login='root', password='default')
  await link.connection(Connection.Server)
  await link.flushall()
  
  # Inserts item into 'list1'
    
  try:
     print (await link.lpush("list1", "item"))
  except Exception as error:     
     print(error.message)

  # Returns all items on list 'list1'

  try:
     for item in (await link.lget("list1")):
        print(item)
  except Exception as error:
     print(error.message)

  # Returns all lists

  try:
     for item in (await link.lkeys("*")):
        print(item)
  except Exception as error:
     print(error.message)

  # Returns last item from 'list1'
    
  try:
     print (await link.lback("list1"))
  except Exception as error:     
     print(error.message)

  # Counts items on 'list1'
    
  try:
     print (await link.lcount("list1"))
  except Exception as error:     
     print(error.message)

  # Resizes 'list1' to 1
    
  try:
     print (await link.lresize("list1", 1))
  except Exception as error:     
     print(error.message)

  # Deletes item from 'list1'
    
  try:
     print (await link.ldel("list1", "item"))
  except Exception as error:     
     print(error.message)


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())