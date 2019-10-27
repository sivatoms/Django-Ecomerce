from .models import Profile
from django import forms
from django.utils.translation import gettext as _

class DateInput(forms.DateInput):
    input_type = 'date'

class EditProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(label=_('Profile pic'),required=False, error_messages = {'invalid':_("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'phone_number',
            'profile_pic',
        )
        widgets = {
            'date_of_birth':DateInput(),
        }