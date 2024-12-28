from django import forms
from .models import Folder
from django.contrib.auth.models import User

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

    parent = forms.ModelChoiceField(queryset=Folder.objects.all(), widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        # Ensure we can pass the current user to the form
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        parent = self.cleaned_data.get('parent')
        
        # Set owner to the passed user (from view)
        owner = self.user

        # Check if a folder with the same name, parent, and owner already exists
        if Folder.objects.filter(name=name, parent=parent, owner=owner).exists():
            raise forms.ValidationError('A folder with this name already exists under the selected parent.')

        return name

class FolderRenameForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
