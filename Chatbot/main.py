from chatterbot.trainers import ListTrainer #train the chatbot
from chatterbot import ChatBot # This will import the chatterbot
import os

bot = ChatBot('Test') # create the chatbot



bot.set_trainer(ListTrainer) # set the trainer

for _file in os.listdir('chats'):
	chats = open('chats/' + _file, 'r').readlines()

	bot.train(chats)

while True:
	request = input('You: ')
	response = bot.get_response(request)
	if float(response.confidence) > 0.5:
		print('Bot: ' + str(response))

	else:
		print('Bot: I do not understand!')