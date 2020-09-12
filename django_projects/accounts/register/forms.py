from django import forms
from register.models import Profile, Account

class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats=['%d/%m/%Y']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [
            'FirstName',
            'MiddleName',
            'LastName',
            'Address1',
            'Address2',
            'City',
            'State',
            'Country',
            'PinCode',
            'DOB',
            'ContactNumber',
            'Occupation',
            'docImage'
        ]
        widgets = {
            'DOB': DateInput()
        }

    def save(self, commit=True) :
        instance = super(ProfileForm, self).save(commit=False)

        if commit:
            instance.save()
        return instance

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account

        fields = [
            'AccountType',
            'Currency',
        ]