# python-beryl - Python Driver for BerylDB.
# http://www.beryldb.com
#
# This is an example script for python-beryl. You may modify it
# and freely use it at your convenience. Feel free to join our
# discord support server If you are interested about BerylDB.

version = "0.1"

import asyncio
import sys
sys.path.insert(0,'..')

from beryl import Client
from beryl.enums import Connection

async def main():
     print("Version: " + str(version))

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())