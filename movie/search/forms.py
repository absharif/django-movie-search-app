from django import forms

class SearchForm(forms.Form):
    CHOICES = (
        ('', '----'),
        ('2', 'Action'),
        ('2', 'Comedy'),
        ('2', 'Drama'),
        )

    title = forms.CharField(max_length=30, required=False)
    year = forms.IntegerField(required=False)
    genre = forms.ChoiceField(choices=CHOICES, required=False)

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        title = cleaned_data.get('title')
        year = cleaned_data.get('year')
        genre = cleaned_data.get('genre')
        if not title and not year and not genre:
            raise forms.ValidationError('You have to input any of these field')