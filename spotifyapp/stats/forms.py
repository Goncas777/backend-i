from django import forms
from django.contrib.auth.models import User
from stats.models import UploadedFile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def clean_password2(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("password2"):
            raise forms.ValidationError("As senhas não coincidem.")
        return self.cleaned_data.get("password2")

class UploadFileForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = UploadedFile
        fields = ['file']  # Apenas o campo do ficheiro