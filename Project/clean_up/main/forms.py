from django import forms
from .models import Application


class MainForm(forms.ModelForm):
    CHOICES = (
        (None, 'Выбери услугу'),
        ('Уборка коттеджа', 'Уборка коттеджа'),
        ('Уборка дома', 'Уборка дома'),
        ('Уборка офиса', 'Уборка офиса'),
        ('Уборка квартиры', 'Уборка квартиры')
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}), label=False)
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}), label=False)
    service = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={'class': 'custom-select'}), label=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label=False)

    class Meta:
        model = Application
        fields = ['name', 'phone', 'service', 'comment']




