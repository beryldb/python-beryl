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

class BaseException(Exception):
    pass

class ClientError(BaseException):
    pass

class ConnectionClosed(ClientError):
    pass

class ServerError(BaseException):
    pass
