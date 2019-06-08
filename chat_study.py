from rest_framework import serializers
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class 채팅마디(self):
  chatbot = ChatBot('O_madie', read_only=True)

# Create a new trainer for the chatbot
  trainer = ListTrainer(chatbot)

# Train the chatbot based on the english corpus
  trainer.train([
    '안녕', '잘 지냈어?', '엉, 잘 지냈어','그럼, 잘 살아라'])

# Get a response to an input statement
  def 응답(self):
    response = chatbot.get_response("안 녕")
    print("한마디: ", response)


chat = 채팅마디
chat.응답