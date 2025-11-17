import django_filters
from django import forms
from django_filters import CharFilter


from jobapp.models import JobPost, ShortlistedCandidate, Recruiter, Job_Seeker


class JobFilter(django_filters.FilterSet):
    title = CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'Search',
                                                                                     'class':"form-control bg-dark border-0" }))

    class Meta:
        model = JobPost
        fields = ('title',)


class ShortlistFilter(django_filters.FilterSet):
    seeker__name = CharFilter(
        label="",
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={
            "placeholder": "Search","class": "form-control bg-dark border-0"
        })
    )

    class Meta:
        model = ShortlistedCandidate
        fields = ("seeker__name",)



class RecruiterFilter(django_filters.FilterSet):
    name = CharFilter(
        label="",
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder':'Search',
            'class':'form-control bg-dark border-0'
        })
    )

    class Meta:
        model = Recruiter
        fields = ('name',)


class SeekerFilter(django_filters.FilterSet):
    name = CharFilter(
        label="",
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder':'Search',
            'class':'form-control bg-dark border-0'
        })
    )

    class Meta:
        model = Job_Seeker
        fields = ('name',)

