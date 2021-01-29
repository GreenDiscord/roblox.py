# Documention For Roblox.py
(note, im not doing anything to do with cookies!)

# Quick Setup

You have to first define the client, which you do py using the "Client" attribute in roblox.py

```py
roblox = Client()
```
Optional args:
  Cookies, Allows you to join games, eg the main features of roblox.py

Next this lib is async so we need to define the function!

```py
async def main():
```
Note : If your using discord.py, you have to define ```ctx``` in the brackets!

Now for the juicy stuff!

# Player Info

```py
roblox.get_user_by_id()
```
Args:
  Int : Roblox user id
  
  
  
  
```py
roblox.get_user_by_name()
```
Args:
  Text : Roblox user name
  
  
  
  
```py
PlayerInfo.name
```
Args:
   None
Returns:
   PlayerInfo Defined Name
   
   
   
   
```py
PlayerInfo.id
```
Args:
  None
Returns:
  PlayerInfo Defined ID
  
  
  
  
```py
PlayerInfo.description
```
Args:
  None
Returns:
   PlayerInfo Defined Description
   
   
   

```py
await PlayerInfo.friends()
```
Args:
  Not Known
Returns:
   PlayerInfo Defined Friends List 

Note : For friend count, use the built in method ```PlayerInfo.friends_count```, if that doesn't work, use len() on the Function Above.




```py
PlayerInfo.is_banned()
```
Args:
  None
Returns:
  True or false, depending on if the user is banned or not.
  
  
  
  
```py
await PlayerInfo.avatar()
```
Args:
  None
Returns:
   URL for PlayerInfo Defined avatar
   


