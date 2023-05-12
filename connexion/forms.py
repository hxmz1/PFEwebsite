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

    def is_valid(self, request):
        identifiant = self.data['identifiant']
        mot_de_passe = self.data['mot_de_passe']
        if User.objects.filter(username=identifiant).exists():
            # Here, we assign the result of authenticate() to a variable
            user = authenticate(request, username=identifiant,
                                password=mot_de_passe)
            if user is None:
                self.add_error(
                    "mot_de_passe", "Les mots de passe ne correspondent pas.")
        else:
            self.add_error("pseudo", "Ce compte n'existe pas.")
        return super(LoginasClient, self).is_valid()


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



