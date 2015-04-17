from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ["email"]