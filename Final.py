import glob
from discord_webhook import DiscordWebhook

Durl=""
a=glob.glob('*.png')
for x in a:
    webhook = DiscordWebhook(url=Durl)
    with open(x, "rb") as f:
        webhook.add_file(file=f.read(), filename="test.png")
    response = webhook.execute(remove_embeds=True)
