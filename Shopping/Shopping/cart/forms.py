from .models import Profile
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'phone_number',
        )
        widgets = {
            'date_of_birth':DateInput(),
        }