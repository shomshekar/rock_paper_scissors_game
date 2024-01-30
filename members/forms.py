from django import forms

# Create the FormName class
class FormName(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()

class FormSelect(forms.Form):
    CHOICES = (('rock', 'Rock'),('paper', 'Paper'),('sciccers', 'Sciccers'),)
    choice = forms.ChoiceField(choices=CHOICES)