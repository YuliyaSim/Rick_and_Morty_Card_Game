from django.forms import Form, CharField, EmailField, PasswordInput, EmailInput, ModelForm, TextInput, Select

from profile_app.models import Profile



class RegisterForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-75'
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control w-75'
    }))
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-75'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-75'
    }))


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'planet': Select(attrs={'class': 'form-control w-75'}),
            'gender': Select(attrs={'class': 'form-control w-75'}),
            'species': Select(attrs={'class': 'form-control w-75'}),
            'status': Select(attrs={'class': 'form-control w-75'}),
            'type': Select(attrs={'class': 'form-control w-75'}),

        }


