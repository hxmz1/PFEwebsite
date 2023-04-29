from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

"""formulaire client"""

class LoginasClient(forms.Form):
    identifiant  = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'pseudo',
                'name': 'pseudo',
                'placeholder': 'id',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px"
            }
        )
    )
    mot_de_passe = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Mot de passe',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get('identifiant')
        mot_de_passe = cleaned_data.get('mot_de_passe')

        if User.objects.filter(username=id).exists():
            user = authenticate(username=id, password=mot_de_passe)
            if user is None:
                raise forms.ValidationError(
                    "Les mots de passe ne correspondent pas.",
                    code='invalid_password'
                )
        else:
            raise forms.ValidationError(
                "Ce compte n'existe pas.",
                code='invalid_username'
            )

        cleaned_data['user'] = user
        return cleaned_data


"""# views.py
def connxionClient(request):
    if request.method == 'POST':
        form = LoginasClient(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('home')
    else:
        form = LoginasClient()

    return render(request, 'loginclient.html', {'form': form})"""

    

"""formulaire superviseur"""


class LoginasSuperviseur(forms.Form):
    pseudo = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'pseudo',
                'name': 'pseudo',
                'placeholder': 'Pseudo',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px"
            }
        )
    )
    mot_de_passe = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Mot de passe',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px"
            }
        )
    )

    def is_valid(self, request):
        pseudo = self.data['pseudo']
        mot_de_passe = self.data['mot_de_passe']
        if User.objects.filter(username=pseudo).exists():
            # Here, we assign the result of authenticate() to a variable
            user = authenticate(request, username=pseudo,
                                password=mot_de_passe)
            if user is None:
                self.add_error(
                    "mot_de_passe", "Les mots de passe ne correspondent pas.")
        else:
            self.add_error("pseudo", "Ce compte n'existe pas.")
        return super(LoginasSuperviseur, self).is_valid()



