import datetime
from xml.dom import ValidationErr
from django import forms
from core.models import Appeal,Applicant,Emergency


class AddAppealForm(forms.ModelForm):
    OPTIONS = (
        Emergency.objects.all().values_list('id','name')
    )
    emergency =  forms.MultipleChoiceField(label='Экстренная служба',widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['application'].empty_label = "Не выбрано"
        
    class Meta:
        model = Appeal
        fields = '__all__'


class AddApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        widgets = {'health': forms.Textarea}

    def  clean_birth(self):
        now = datetime.datetime.now().date()
        birth = self.cleaned_data['birth']
        if birth > now:
            raise ValidationErr('Год рождения заявителя не может быть в будущем')
        return birth

    def  clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if len(telephone) > 11:
            raise ValidationErr('Длина номера телефона не может быть длинее 11 символов')
        return telephone


class AddEmergencyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Не выбрано"
        
    class Meta:
        model = Emergency
        fields = '__all__'
        help_texts = {
            'code': 'Код должен состоять из 2 или 3 цифр'
        }