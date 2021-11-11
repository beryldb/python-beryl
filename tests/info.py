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
  
  # Returns database size
    
  try:
     print (await link.dbsize())
  except Exception as error:     
     print(error.message)
     
  # Returns current select
  
  try:
     print (await link.current())
  except Exception as error:     
     print(error.message)

  # Returns current version
  
  try:
     print (await link.version())
  except Exception as error:
     print(error.message)

  # Current database
  
  try:
     print (await link.db())
  except Exception as error:
     print(error.message)


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())