from pyrogram import Client, filters

bot_token = "6800419925:AAHNpxtnC651xdjwqTAkeU2iD5C-Vi88uu4"

api_id = 27596357
api_hash = "6332fa4e311625ad32a403349cb41ed9"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

