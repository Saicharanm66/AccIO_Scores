from django import forms
from .models import Team, TeamMember
class CustomFooForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ('teamname','player_img', 'player_name',  'Player_type', 'Player_side')
        widgets = {
            'teamname': forms.TextInput(),
        }