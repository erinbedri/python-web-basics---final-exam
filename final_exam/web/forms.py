from django import forms

from final_exam.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')


class EditProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'picture')


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')


class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')
        widgets = {
            'type': forms.TextInput(attrs={'disabled': True}),
            'model': forms.TextInput(attrs={'disabled': True}),
            'year': forms.TextInput(attrs={'disabled': True}),
            'image_url': forms.URLInput(attrs={'disabled': True}),
            'price': forms.TextInput(attrs={'disabled': True}),
        }
