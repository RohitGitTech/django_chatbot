# chatbot_app/views.py
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
bot_json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bot.json')

with open(bot_json_path, 'r') as json_file:
    responses = json.load(json_file)
conversation = []

def chatbot_response(user_input):
    user_input = user_input.lower()

    for category, category_responses in responses.items():
        if user_input in category_responses:
            return category_responses[user_input]

    return responses["default"]

# @csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']

        conversation.append(f"You : {user_input}")

        bot_response = chatbot_response(user_input)

        conversation.append(f"Chatbot : {bot_response}")

    if request.method == 'GET':
        conversation.clear()

    return render(request, 'chatbot_app/chat.html', {'conversation': conversation})
