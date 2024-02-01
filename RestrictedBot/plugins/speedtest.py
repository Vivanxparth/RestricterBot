from pyrogram import Client, filters
import speedtest
import matplotlib.pyplot as plt
from io import BytesIO
from RestrictedBot import app

# Initialize the Speedtest client
st = speedtest.Speedtest()

# Define a handler for the /speedtest command
@app.on_message(filters.command("speedtest"))
async def speedtest_command(client, message):
    await message.reply_text("Running Speedtest")
    # Perform the speed test
    st.get_best_server()
    download_speed = st.download()
    upload_speed = st.upload()

    # Create a visual representation of the speed test results
    plt.bar(["Download", "Upload"], [download_speed / 1_000_000, upload_speed / 1_000_000])
    plt.title("Speed Test Results")
    plt.ylabel("Speed (Mbps)")
    plt.ylim(0, max(download_speed, upload_speed) / 1_000_000 + 10)
    plt.savefig("speed_test_results.png")
    plt.close()

    # Send the speed test results as a photo
    caption = f"Download speed: {download_speed / 1_000_000:.2f} Mbps\nUpload speed: {upload_speed / 1_000_000:.2f} Mbps"
    with open("speed_test_results.png", "rb") as speed_test_img:
        app.send_photo(
            chat_id=message.chat.id,
            photo=speed_test_img,
            caption=caption
        )
