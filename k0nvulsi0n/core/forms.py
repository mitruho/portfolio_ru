from django import forms

class ContactForm(forms.Form):
    contact_email = forms.EmailField(label="Your Email", max_length=100)
    contact_phone = forms.CharField(label="Your Phone Number", max_length=15, required=False)
    project_title = forms.CharField(label="Project Title", max_length=100)
    project_description = forms.CharField(widget=forms.Textarea, label="Project Description")
