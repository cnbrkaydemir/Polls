from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control'}))

    last_name = forms.CharField(label='Last Name', max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control'}))
    email = forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                              'class': 'form-control'}))

    date_of_birth = forms.DateField(label='Date of Birth',
        widget=forms.DateInput(attrs={'placeholder': 'Date of Birth', 'class': 'form-control', 'type': 'date'})
    )

    gender = forms.ChoiceField(
        label='Gender',
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ],
        widget=forms.RadioSelect()
    )

    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                              'class': 'form-control'}))

    password2 = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password',
                                                              'class': 'form-control'}))



class LoginForm(forms.Form):
    email = forms.EmailField(label='Username', max_length=100, required= True,
                               widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                             'class': 'form-control'}))

    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control'}))