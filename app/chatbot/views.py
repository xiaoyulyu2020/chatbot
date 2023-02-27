from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        user_input = request.POST.get('user_input')
    return render(request, "main.html", {})
