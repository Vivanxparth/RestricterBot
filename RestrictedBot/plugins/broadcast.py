from pyrogram import Client, filters
from RestrictedBot import app as bot

@bot.on_message(filters.command(['broadcast']))
def broadcast_message(client, message):
    if message.chat.type == 'private':
       await bot.reply_text(message, "This command can only be used in a group or channel.")
        return

    # Get the message to broadcast
    broadcast_text = message.text[11:]  # Remove '/broadcast ' from the command

    # Get the chat ID of the group or channel
    chat_id = message.chat.id

    # Get all members of the group or channel
    members = bot.get_chat_members_count(chat_id)

    # Send the message to each member
    for i in range(members):
        try:
            bot.send_message(chat_id, broadcast_text)
        except Exception as e:
            print(e)

   await bot.reply_text(message, "Broadcast sent successfully!")
