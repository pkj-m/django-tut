from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # what additional fields do we want for this form?
    email = forms.EmailField() #default: required = True 
    first_name = forms.Field()
    last_name = forms.Field()

    class Meta:
        model = User  # model with which this form interacts
        # everytime this form validates, it creates a new User object

        # the fields to be displayed in the form, in the respective order
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']



# a model form is a form which works with a specific database model
# I cannot update the profile picture from this model because this model does not actually have the
# profile picture. Therefore, to update the profile, we create a new profile update form below
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField() 
    first_name = forms.Field()
    last_name = forms.Field()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email'] 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

