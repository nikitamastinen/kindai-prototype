import asyncio

from langchain.chat_models.gigachat import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage
from aiogram import Bot, Dispatcher, types

giga = GigaChat(
    profanity=False,
    credentials="ZWRhMWMxODgtMGJiZi00NDM0LThjYWMtNDBiZDM0NmEzYTA0OjlhOTYzMWE3LWI4ODAtNGFkZi04OWExLTc3N2E4NmIyODgwYg==",
    scope="GIGACHAT_API_PERS",
    verify_ssl_certs=False
)

messages = [
    SystemMessage(
        content="""
        Ты бот, который соедит за настроением сотрудников в чате. Нужно оценивать отзывчивость и токсичность сотрудников и давать рекомендацию в HR. отвечать на каждое сообщение шаблоном:
        {
        уровень отзывчивости:  {число от -10 до 10};
        уровень токсичности: {число от -10 до 10};
        рекомендация HR: Сотрудник такой-то требует внимания;
        рекомендация сотруднику: Привет На этой неделе вы были очень добры: Вот совет #совет, который поможет вашим коллегам быть более отзывчивыми к вам. Рассмотрите возможность задавать открытые вопросы, чтобы стимулировать углубленное обсуждение.;
        }
        """
    )
]


bot = Bot(token="5771137683:AAEbqmUH8xauH1PH-g7qcrtSIPOF5F5Bozo")
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(message: types.Message):
    # Reply to the message
    messages.append(HumanMessage(content="Оцени это сообщение: " + message.text))
    res = giga(messages)
    messages.append(res)
    print(res.content)
    
    await message.reply(res.content)


def main():
    # Start the bot
    try:
        asyncio.run(dp.start_polling())
    finally:
        dp.stop_polling()


if __name__ == '__main__':
    main()


