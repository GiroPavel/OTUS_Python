from django import forms
from .models import Clean


class BookForm(forms.ModelForm):
    CHOICES_SERVICE = (
        (None, 'Выбери услугу'),
        ('Уборка коттеджа', 'Уборка коттеджа'),
        ('Уборка дома', 'Уборка дома'),
        ('Уборка офиса', 'Уборка офиса'),
        ('Уборка квартиры', 'Уборка квартиры')
    )

    CHOICES_TYPECLEAN = (
        (None, 'Тип Уборки'),
        ('Пропылесосить', 'Пропылесосить'),
        ('Протереть пол', 'Протереть пол'),
        ('Отполировать мебель', 'Отполировать мебель')
    )

    CHOICES_ROOMS = (
        (None, 'Комната'),
        ('Гостинная', 'Гостинная'),
        ('Кухня', 'Кухня'),
        ('Прихожая', 'Прихожая'),
        ('Ванная', 'Ванная')
    )

    place = forms.CharField(widget=forms.Select(choices=CHOICES_SERVICE, attrs={'class': 'custom-select'}), label=False)
    type_clean = forms.CharField(widget=forms.Select(choices=CHOICES_TYPECLEAN, attrs={'class': 'custom-select'}),
                                 label=False)
    type_rooms = forms.CharField(widget=forms.Select(choices=CHOICES_ROOMS, attrs={'class': 'custom-select'}),
                                 label=False)

    class Meta:
        model = Clean
        fields = ['place', 'type_clean', 'type_rooms']
