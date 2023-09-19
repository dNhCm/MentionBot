
import config
from pyrogram import Client, filters, types, enums

# Init bot
bot = Client('MentionBot',
             api_id=config.API_ID,
             api_hash=config.API_HASH,
             bot_token=config.BOT_TOKEN
             )


# Mention func of bot
@bot.on_message(filters.group & filters.command('all'))
async def mention(client: Client, message: types.Message):
    # Getting users
    chat = await client.get_chat(message.chat.id)
    users = client.get_chat_members(chat.id)

    # Preparing mention text
    text = ' '.join(message.text.split(' ')[1:]) + '\n\n' + ' '.join(
        [f'[{user.user.first_name}](tg://user?id={user.user.id})' async for user in users])

    # Mention magic
    await message.delete()
    await client.send_message(chat_id=chat.id, text=text, parse_mode=enums.ParseMode.MARKDOWN)


# Main
def main():
    bot.run()


if __name__ == '__main__':
    main()
