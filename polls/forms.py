from django import forms

class PollForm(forms.Form):
    question = forms.CharField(label='Poll Question', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': ' Poll Question'}))

    description = forms.CharField(label='Poll Description', required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': ' Poll Description'}))

    option1 = forms.CharField(label='Option 1', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control mb-2',
                                                            'placeholder': ' Choice 1'}))

    option2 = forms.CharField(label='Option 2', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control mb-2',
                                                            'placeholder': ' Choice 2'}))

    option3 = forms.CharField(label='Option 3', required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control mb-2',
                                                            'placeholder': ' Choice 3 (Optional)'}))

    option4 = forms.CharField(label='Option 4', required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control mb-2',
                                                            'placeholder': ' Choice 4 (Optional)'}))

