from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            stop='.',
            temperature=0.5,
        )
        print(response)
        chatbot_response = response['choices'][0]['text']
    return render(request, "app/main.html", {'response': chatbot_response})
