from django import forms
from accounts.models import Profile


class UserUpdateSelection(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('filter_city',)
