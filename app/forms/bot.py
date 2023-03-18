from django import forms


class UpdatePlayerForm(forms.Form):
    unique_name = forms.CharField(label='机台别名')
    player_count = forms.IntegerField(label='排队人数')
