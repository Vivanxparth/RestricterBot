import speedtest
from pyrogram import Client, filters
from RestrictedBot import app, OWNER_ID

speedtester = speedtest.Speedtest()

# Define the speedtest command
@app.on_message(filters.command("speedtest") & filters.group)
async def run_speedtest(client, message):
    # Check if the user is the bot owner
    if message.from_user.id == OWNER_ID:
      command, *text = message.text.split(maxsplit=1)
      text = text[0]
      speedtester.get_best_server()
      download_speed = speedtester.download()
      upload_speed = speedtester.upload()
      ping = speedtester.results.ping

    speedtest_result = f"Download Speed: {download_speed / 1024 / 1024:.2f} Mbps\nUpload Speed: {upload_speed / 1024 / 1024:.2f} Mbps\nPing: {ping:.2f} ms"
    await message.reply_text(speedtest_result)

