from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
# from .models import *
# from .forms import ContactForm
import google.generativeai as genai
from django.http import HttpResponseRedirect, JsonResponse
from .models import ChatBot
from django.contrib.auth.decorators import login_required

genai.configure(api_key="AIzaSyDK5Zpvg5GE3xOoALJdCK2oYBw73fZS4u4")

@login_required
def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(text)
        user = request.user
        ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)
        # Extract necessary data from response
        response_data = {
            "text": response.text,  # Assuming response.text contains the relevant response data
            # Add other relevant data from response if needed
        }
        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(
            reverse("chat")
        )  # Redirect to chat page for GET requests

@login_required
def chat(request):
    user = request.user
    chats = ChatBot.objects.filter(user=user)
    return render(request, "chat_bot.html", {"chats": chats})



def home(request):
    # if request.method == "POST":
    #     form  = ContactForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']
    #         form.save()
    #         return redirect("thank-you")
        
    # else:
    #     form = ContactForm()
        
    return render(request, "index.html")

def skorboard(request):
    return render(request, "skorboard.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def elements(request):
    return render(request, "elements.html")


def gallery(request):
    return render(request, "gallery.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def news(request):
    return render(request, "news.html")


def staff(request):
    return render(request, "staff.html")