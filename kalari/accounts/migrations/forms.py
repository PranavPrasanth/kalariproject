from django import forms
from account.models import mykalari,users


class signupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']
        help_texts = {
            'username': None,
             }

 class CommonForm(forms.ModelForm):
            """Form definition for Common."""

            class Meta:
                """Meta definition for Commonform."""

                model = User
                fields = ('first_name', 'last_name', 'email')


class AuthForm(forms.ModelForm):
    """Form definition for Auth."""

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """Meta definition for Authform."""

        model = User
        fields = ('username','password')
        widget = {
            'password': forms.PasswordInput(),
        }
        help_texts ={
            'username': None
        }


 class EditProfileForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email', 'username']
            help_texts = {
                'username': None,

            }


class mykalariForm(forms.ModelForm):
    """Form deefinition for Company """

    class Meta:
        """Meta definition for Companyform"""
        model = mykalari
        exclude = ['user']


class usersForm(forms.ModelForm):
    """Form deefinition for Company """

    class Meta:
        """Meta definition for Companyform"""
        model = users
        exclude = ['user']
