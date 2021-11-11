<p align="center">
  <img src="https://static.beryl.dev/smaller.png">
</p>

# python-beryl, a Python driver for BerylDB.

[![Mailing List](https://img.shields.io/badge/email-google%20groups-4285F4 "beryldb@googlegroups.com")](https://groups.google.com/g/beryldb)
[![Twitter](https://img.shields.io/twitter/follow/beryldb?color=%23179CF0&logo=twitter&style=flat-square "@beryldb on Twitter")](https://twitter.com/beryldb)
[![Discord Server](https://badgen.net/badge/icon/discord?icon=discord&label)](https://discord.gg/23f6w9sgAd)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
<br>


If you want to learn more about BerylDB and how to install it, feel free to check our
documentation at [docs.beryl.dev](https://docs.beryl.dev/).<br>
Follow us on [Twitter](https://twitter.com/beryldb).

## QuickStart

The quick start guide will show you how to set up a simple application using
BerylDB's Python driver.

It scope is only how to set up the driver and perform the simple operations.
For more advanced coverage, we encourage reading our tutorial.

## Connecting to BerylDB

Let's create a new **example.py** file that we will be using to show
basic operations. First, we need to add code to conenct to the remote
server:

```python
async def main():
  link = Client(host='127.0.0.1', port=6378, login='root', password='default')
  await link.connection(Connection.Server)
```

If you are familiar with BerylDB, you will soon learn that most functions
from this driver have the same name as its underlying function. 

Check BerylDB's [full list of commands](https://docs.beryl.dev/commands/)

## Querying

Let's look at an example exercising all the different available operations.

We define a key **``hello``** with value **world**

```python
try:
    print (await link.set("hello", "world"))
except Exception as error:     
    print(error.message)
```

Let's try setting a map

```python
try:
    print (await link.hset("a", "b", "c"))
except Exception as error:     
    print(error.message)
```

These two code will have the following output (assuming that neither 'hello'
or 'a' are defined):

```
OK
```

In BerylDB, different structues cannot hold the same variable name. In order
to check what kind of data structure is a given key, you may use type

```python
print (await link.type("a")) # Key
```

## Querying for lists

You can use forEach in order to iterate a result that contains more than one
item:

```python
try:
    for item in (await link.keys("*")):
       print(item)
except Exception as error:     
    print(error.message)
```

Assuming that keys **``a``** and **``b``** are defined, this code will have the following output

```
a
b
```

## Contributing

We are always welcoming new members. If you wish to start contributing code to the 
Beryl project in any form, such as in the form of pull requests via Github, 
a code snippet, or a patch, you will need to agree to release your work under the terms of the
BSD license.

## External Links

* [Documentation](https://docs.beryl.dev)
* [GitHub](https://github.com/beryldb/beryldb)
* [Support/Discord](https://discord.gg/23f6w9sgAd)
* [Twitter](https://twitter.com/beryldb)

