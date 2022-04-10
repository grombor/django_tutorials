from django import forms

class ReviewForm(forms.Form):

    user_name = forms.CharField(
        label="Your name",
        max_length=100,
        min_length=2,
        error_messages={
            "required": "Your name must not be empty",
            "max_lenght": "Please enter a shorter name"
    })

    review_text = forms.CharField(
        label="Your review",
        max_length=200,
        widget=forms.Textarea
        )

    rating = forms.IntegerField(
        label="Your rating",
        min_value=1,
        max_value=5
    )