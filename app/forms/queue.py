from django import forms


class UpdatePlayerForm(forms.Form):
    cabinet_id = forms.IntegerField(label='机台ID')
    player_count = forms.IntegerField(label='排队人数')
