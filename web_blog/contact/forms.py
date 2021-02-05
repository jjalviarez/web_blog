from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name',required=True, max_length=100)
    email = forms.EmailField(label='email',required=True)
    content = forms.CharField(widget=forms.Textarea)




