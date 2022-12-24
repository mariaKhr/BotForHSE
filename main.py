from telebot.async_telebot import AsyncTeleBot
import telebot
import asyncio
bot = AsyncTeleBot('token')


@bot.message_handler(commands=["start"])
async def start(message):
    await bot.send_message(message.chat.id, "This is a bot telling about the holidays in the last week of December, "
                                            "send /help to know more")


@bot.message_handler(commands=["help"])
async def help(message):
    await bot.send_message(message.chat.id, "if you want to find out what holidays are in the last week of December, "
                                            "send: /dec25, /dec26, /dec27, /dec28, /dec29, /dec30 or /dec31")


@bot.message_handler(commands=['dec25'])
async def dec25(message):
    await bot.send_message(message.chat.id, "Christmas")
    await bot.send_message(message.chat.id, "The great thing about Christmas is that there is "
                                            "a joyful festivity for everyone to enjoy.")


@bot.message_handler(commands=['dec26'])
async def dec26(message):
    await bot.send_message(message.chat.id, "Boxing Day")
    await bot.send_message(message.chat.id, "In the U.K., Boxing Day is known as a "
                                            "shopping holiday, much like Black Friday.")


@bot.message_handler(commands=['dec27'])
async def dec27(message):
    await bot.send_message(message.chat.id, "National Fruitcake Day")
    await bot.send_message(message.chat.id, "A day for lovers of fruitcake to rejoice in the delights of the most "
                                            "misunderstood fruit.")


@bot.message_handler(commands=['dec28'])
async def dec28(message):
    await bot.send_message(message.chat.id, "National Call a Friend Day")
    await bot.send_message(message.chat.id, "Call that friend you've been meaning to get back in touch with.")


@bot.message_handler(commands=['dec29'])
async def dec29(message):
    await bot.send_message(message.chat.id, "Constitution of Ireland")
    await bot.send_message(message.chat.id, "The Constitution of Ireland is a document that defines the rights "
                                            "of the people.")


@bot.message_handler(commands=['dec30'])
async def dec30(message):
    await bot.send_message(message.chat.id, "National Bacon Day")
    await bot.send_message(message.chat.id, "If you want to scream at the top of your lungs, “I love bacon,” join us!")


@bot.message_handler(commands=['dec31'])
async def dec31(message):
    await bot.send_message(message.chat.id, "New Year's Eve")
    await bot.send_message(message.chat.id, "The last day of the last month of what usually feels like the longest "
                                            "year ever.")


bot.add_custom_filter(telebot.asyncio_filters.ChatFilter())
asyncio.run(bot.polling())
