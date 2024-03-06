from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon import functions, types
 # developer: termux_community_uz
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
 #termux_devs
client = TelegramClient('me', api_id, api_hash)
 #github_project
@client.on(events.NewMessage(outgoing=True, pattern='\.ref'))
async def nq(event):
    result = await client(functions.messages.StartBotRequest(
        bot='sms_vakbot',
        peer='sms_vakbot',
        start_param='user3173'
    ))
  
 
client.start()
print("run")
client.run_until_disconnected(
