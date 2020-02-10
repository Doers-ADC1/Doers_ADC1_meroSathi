from django import forms
from userprofile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     # class Meta:
#     #     model = Profile
#     #     fields = ['profile_image']
#     profile_image = forms.FileField()
#
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         # user.first_name = self.cleaned_data['first_name']
#         # user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#
#         user.save()
#         user.create_profile()
#
#         # user.profile_image = self.cleaned_data.get('profile_image')
#         # user.profile.save()
#
#         if commit:
#             user.save()


# class RegForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model = User
#         fields = ('username', 'password', 'email')
#
#
# class ProfileForm(forms.ModelForm):ccounts/signup/
#     class Meta():
#         model = Profile
#         fields = ('student_id', 'photo')
