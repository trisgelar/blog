from django import forms

class EmailPostForm(forms.Form):
	name = forms.Charfield(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.Charfield(required=false, widget=forms.Textarea)