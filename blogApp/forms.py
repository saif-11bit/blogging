from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name','class':'form-control'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email','class':'form-control'}))
	phone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number','class':'form-control'}))
	message = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':4, 'cols':15,'placeholder': 'Enter your message','class':'form-control'}))


class SubscribeForm(forms.Form):
	email = email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email','class':'form-control searchInput'}))