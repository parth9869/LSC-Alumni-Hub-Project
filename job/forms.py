import imp
from django import forms
from .models import jobs

class postForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['companyname'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['category'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['type'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['location'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['minSalary'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['maxSalary'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['description'].widget.attrs.update({'class':'form-control rounded-3 customPosttext','rows':5})
        self.fields['responsibilities'].widget.attrs.update({'class':'form-control rounded-3 customPosttext','rows':5})
        self.fields['qulifications'].widget.attrs.update({'class':'form-control rounded-3 customPosttext','rows':5})
        self.fields['companydetail'].widget.attrs.update({'class':'form-control rounded-3 customPosttext','rows':5})
        self.fields['noOfvacancy'].widget.attrs.update({'class':'form-control rounded-3'})
        self.fields['url'].widget.attrs.update({'class':'form-control rounded-3 '})
        self.fields['postby'].widget=forms.HiddenInput()
    
    class Meta:
        model=jobs
        fields=['title','companyname','category','type','location','minSalary','maxSalary','description','responsibilities','qulifications','companydetail','noOfvacancy','url','postby']