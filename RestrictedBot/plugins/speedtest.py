import speedtest
from pyrogram import Client, filters
from RestrictedBot import app




speedtester = speedtest.Speedtest()

# Define the speedtest command
@app.on_message(filters.command("speedtest"))
async def run_speedtest(client, message):
    speedtester.get_best_server()
    download_speed = speedtester.download()
    upload_speed = speedtester.upload()
    ping = speedtester.results.ping

    speedtest_result = f"Download Speed: {download_speed / 1024 / 1024:.2f} Mbps\nUpload Speed: {upload_speed / 1024 / 1024:.2f} Mbps\nPing: {ping:.2f} ms"
    await message.reply_text(speedtest_result)
