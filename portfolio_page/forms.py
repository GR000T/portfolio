from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(
        attrs={'class': 'form-input', 'id': 'name', 'placeholder': 'Your Name'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(
        attrs={'class': 'form-input', 'id': 'email', 'placeholder': 'Your Email'}))
    subject = forms.CharField(label='subject', widget=forms.TextInput(
        attrs={'class': 'form-input', 'id': 'subject', 'placeholder': 'Subject'}))
    message = forms.CharField(label='name', widget=forms.TextInput(
        attrs={'class': 'form-input', 'id': 'message', 'placeholder': 'Type Your Message...'}))

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]

        '''def clean(self):
            email=self.cleaned_data.get('email')
            password=self.cleaned_data.get('password')
            password_confirm=self.cleaned_data.get('password_confirm')'''
