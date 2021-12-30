import datetime

from django.forms import ModelForm, TextInput, DateInput, ModelChoiceField

from proyecto.models import Oficio, Dependencia


class OficioForm(ModelForm):

    dir_remitente= ModelChoiceField(label=u'Dependencia', queryset=Dependencia.objects.all())

    class Meta:
        model = Oficio
        fields = '__all__'
        exclude = ['archivo_datetime', 'creado_por', 'creado_el', 'modi_por', 'modi_el']
        widgets = {
            'fecha_oficio': DateInput(attrs={'type': 'date', 'class': 'form_input', 'value': datetime.date.today().strftime("%Y-%m-%d")}),
        }

    def __init__(self, *args, **kwargs):
        super(OficioForm, self).__init__(*args, **kwargs)
        self.fields['dir_remitente'].queryset = Dependencia.objects.all()
