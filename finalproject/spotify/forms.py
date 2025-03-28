from django import forms


from spotify.models import Task

class TaskForm(forms.ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Task
        fields = ["user","file"]