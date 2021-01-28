# Documention For Roblox.py
(note, im not doing anything to do with cookies!)

# Quick Setup

You have to first define the client, which you do py using the "Client" attribute in roblox.py

```
roblox = Client()
```
Optional args:
  Cookies, Allows you to join games, eg the main features of roblox.py

Next this lib is async so we need to define the function!

```
async def main():
```
Note : If your using discord.py, you have to define ```ctx``` in the brackets!

Now for the juicy stuff!

# Player Info

```
roblox.get_user_by_id()
```
Args:
  Int : Roblox user id
  
```
roblox.get_user_by_name()
```
Args:
  Text : Roblox user name
