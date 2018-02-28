from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from multiprocessing import Process

chatbot = ChatBot("rocRot")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# 使用中文语料库训练它
chatbot.train("chatterbot.corpus.chinese")
# 使用英文语料库训练它
chatbot.train("chatterbot.corpus.english")


def chatter(message):
    chinese = Process(target=chinese_train, args=(message, ))
    # english = Process(target=english_train, args=(message, ))

    chinese.start()
    # english.start()

    return chatbot.get_response(str(message.content)).text


def chinese_train(message):
    chatbot.set_trainer(ListTrainer)
    # 使用用户输入训练它
    chatbot.train(str(message.content))


def english_train(message):
    chatbot.set_trainer(ListTrainer)
    # 使用用户输入训练它
    chatbot.train(message.content.strip().encode('utf-8'))
