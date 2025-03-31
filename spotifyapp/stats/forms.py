import logging
from django import forms
from django.contrib.auth.models import User
from stats.models import UploadedFile

logger = logging.getLogger(__name__)

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        
        if password != password2:
            logger.warning("Password confirmation does not match for user %s", self.cleaned_data.get("username"))
            raise forms.ValidationError("As senhas não coincidem.")
        
        return password2

class UploadFileForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput, required=False)

    class Meta:
        model = UploadedFile
        fields = ['file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            logger.info("File %s uploaded successfully by user %s", instance.file.name, instance.user if instance.user else "Anonymous")
        return instance
