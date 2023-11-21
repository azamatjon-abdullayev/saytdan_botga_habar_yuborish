from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("get_check", "Botni ishlayotganini tekshirish"),
            types.BotCommand("dog", "Botni ishlayotganini tekshirish"),
            types.BotCommand("help", "Yordam"),

        ]
    )
