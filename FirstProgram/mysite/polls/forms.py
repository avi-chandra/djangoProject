from django import forms

class RegistrationForm(forms.Form):
    fullname = forms.CharField(max_length=15)
    idnumber = forms.CharField(required=True, max_length=15)
    age = forms.IntegerField(required=True, max_value=110)
    city = forms.CharField(required=True, max_length=30)
    state = forms.CharField(required=True, max_length=25)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 5:
            raise forms.ValidationError("Not enough words!!")
        return message
