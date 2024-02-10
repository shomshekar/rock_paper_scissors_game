from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
# from django.forms.models import model_to_dict

from . import forms
from .models import Members, GameResult
import random

choice_list = ['rock', 'paper', 'scissors']

def winner(user_action, computer_action):
    data = {}
    if user_action == computer_action:
        data = {
            'winner' : 'Tie',
            'message' : "Both players selected {}. It's a tie!".format(user_action)
        }
    elif user_action == 'rock':
        if computer_action == 'scissors':
            data = {
                'winner' : 'User',
                'message' : "Rock wins over scissors! You win!"
            }
        else:
            data = {
                'winner' : 'Computer',
                'message' : "Paper wins over rock! You lose."
            }
    elif user_action == 'paper':
        if computer_action == 'rock':
            data = {
                'winner' : 'User',
                'message' : "Paper wins over rock! You win!"
            }
        else:
            data = {
                'winner' : 'Computer',
                'message' : "Scissors wins over paper! You lose."
            }
    elif user_action == 'scissors':
        if computer_action == 'paper':
            data = {
                'winner' : 'User',
                'message' : "Scissors wins over paper! You win!"
            }
        else:
            data = {
                'winner' : 'Computer',
                'message' : "Rock wins over scissors! You lose."
            }

    return data


# Create your views here.
def game_set(request, slug):
    if slug == None:
        return redirect("/")
    form = forms.FormSelect()
    member = get_object_or_404(Members, slug=slug)

    template = loader.get_template('game.html')
    context = {
        'form': form,
        'member': member,
    }

    # Check to see if we are getting a POST request back
    if request.method == "POST":
        form = forms.FormSelect(request.POST)
        # Then we check to see if the form is valid
        if form.is_valid():
            # computer randomly selects one item from list
            computer_selection = random.choice(choice_list)
            # Determine the winner
            result = winner(form.cleaned_data['choice'], computer_selection)
            
            gameSet = GameResult(member_id=member, member_selection=form.cleaned_data['choice'], computer_selection=computer_selection, result=result['winner'])
            gameSet.save() 

            context['message'] = result['message']
        else:
            context['message'] = 'Something went wrong! Please try again'

    return HttpResponse(template.render(context, request))


def all_result(request):
    all_result = GameResult.objects.all()
    template = loader.get_template('all_result.html')
    context = {
        'all_result' : all_result
    }
    return HttpResponse(template.render(context, request))

def home(request):
    form = forms.FormName()
    # Check to see if we are getting a POST request back
    if request.method == "POST":
        form = forms.FormName(request.POST)
        # Then we check to see if the form is valid
        if form.is_valid():
            member = Members(firstname=form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'])
            member.save()
            slug = str(member.id)+'-'+member.firstname.lower()+'-'+member.lastname.lower()
            member.slug = slug
            member.save()
            # Redirecting to another url
            return redirect("/view-game/"+slug)

    return render(request, "home.html", {'form':form})