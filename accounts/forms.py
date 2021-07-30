from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm

from .models import ElearningUser,USER_ROLE_CHOICES

class ElearningUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ElearningUser
        fields = ('email', 'username','role',)

class ElearningUserChangeForm(UserChangeForm):

    class Meta:
        model = ElearningUser
        fields = ('email', 'username','role',)


class ElearningSignupForm(SignupForm):
    role = forms.ChoiceField(choices=USER_ROLE_CHOICES)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(ElearningSignupForm, self).save(request)

        user.role=self.cleaned_data['role']
        user.save()



        # You must return the original result.
        return user
