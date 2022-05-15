from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _


class UserForm(ModelForm):

	error_messages = {
		'password_mismatch': _("The two password fields didn't match."),
		'existing_user': _("Username already exists."),
    }
	password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput, 
		help_text=_("Your Password must have atleast 8 characters and cannot be all Integers."))
	password2 = forms.CharField(label=_("Password confirmation"), 
		widget=forms.PasswordInput, 
		help_text=_("Enter the same password as above, for verification."))

	class Meta:

		model = User
		fields = ["username", "email",]

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
            	code='password_mismatch',
            )
		if self.cleaned_data.get("username") in User.objects.all():
			raise forms.ValidationError(
				self.error_messages['existing_user'],
            	code='existing_user',
            )

		return password2

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user




