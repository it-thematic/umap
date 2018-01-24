from django import forms
from django.contrib import admin
from .models import *


class DatalayerStylesForm(forms.ModelForm):
    """
        styles - дополнительное поле -  required= False - необязательное - для хранения выбранных полей
    """
    styles = forms.MultipleChoiceField(required=False, label='стили', choices=(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(DatalayerStylesForm, self).__init__(*args, **kwargs)
        self.fields['styles'].choices = [(style.id, style.title) for style in Styles.objects.all()]
        if self.instance.styles:
            self.initial['styles'] = [int(style) for style in self.instance.styles.split(",")]

    class Meta:
        model = DatalayerStyles
        exclude = ()

    def clean_styles(self):
        data = self.cleaned_data['styles']
        cleaned_data = ",".join(data)
        return cleaned_data


class ForestDatalayerStyleSettingAdmin(admin.ModelAdmin):
    model = DatalayerStyles
    form = DatalayerStylesForm
    list_display = ('datalayer', 'styles')

    fieldsets = [
        (None, {'fields': ['datalayer', ]}),
        ('Отобразить/скрыть поля ', {'fields': ['styles'], 'classes': ['collase']}),
    ]


admin.site.register(Styles)
admin.site.register(DatalayerStyles, ForestDatalayerStyleSettingAdmin)
