from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your Email',
                'class': 'form-control',
            }
        ),
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control',
            }
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your Message...',
                'rows': 5,
                'class': 'form-control',
            }
        ),
    )
