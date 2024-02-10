from django import forms

# Create the FormName class
class FormName(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['style'] = 'width:auto;display:inline-block;'
            


class FormSelect(forms.Form):
    CHOICES = (('rock', 'Rock'),('paper', 'Paper'),('scissors', 'Scissors'),)
    choice = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-select'
            visible.field.widget.attrs['style'] = 'width:auto;display:inline-block;'
