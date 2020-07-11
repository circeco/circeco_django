from django import forms


class SearchShopsForm(forms.Form):
    term = forms.CharField(label="Search for a Circular Initiative here...", required=False)
