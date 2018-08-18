# synapsBot
This is just a personal bot for my server. I hope you can figure out what my code does. Feel welcome to contact me on Discord @Mehvix#7172 


If you keep getting an error code when trying to write to the `users.json` file it's probably because you have multiple versions of the same bot running at the same time.


## Cogs / Files 

### .default_formatting.py

Template for when I make a new cog


### admin.py

Admin-exclusive commands


### basic.py

Very simple commands everyone in the server can use


### createpoll.py
Cog for the .createpoll command. Moved out of `verified.py` because it took up too much space


### curtime.py
Used to track uptime and cur(rent) time


### forwarding.py
Forwards all DM's the bot sends and recieves to the owner (me)


### insults.json
All insults for .insult command (in `verified.py`)
Found this from [TwentySixe's Github](https://github.com/Twentysix26/26-Cogs/blob/master/insult/data/insults.json)


### karma.py
For managing levels and karma (users.json)


### music.py
Simple music bot. Used for when Rythm is down


### notifications.py
Messages for when people join/leave/.accept/are banned from sever


### roulette_outcomes / users.json 
Backups for if anything goes wrong


### settings.py
Where server settings are stored for my main server and my testing server


### verified.py
Verified-exclusive commands (cool-kid stuff)
