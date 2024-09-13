from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email Address')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

    # Optionally, you can add custom validation
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError('Message is too short. It should be at least 10 characters long.')
        return message
