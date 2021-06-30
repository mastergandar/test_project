from django import forms


class MainForm(forms.Form):
    Time = forms.DateField(label='Дата',
                           input_formats=['%d/%m/%Y'],
                           widget=forms.DateInput())
    FLM_SP = forms.CharField(label='ФИО СДЛ', max_length=250)
    FLM_Customer = forms.CharField(label='ФИО сотрудника', max_length=250)
    FLM_Director = forms.CharField(label='ФИО директора', max_length=250)
    Post_Director = forms.CharField(label='Должность руководителя', max_length=100)
    Post_Customer = forms.CharField(label='Должность сотрудника', max_length=100)
    Client_cut = forms.CharField(label='Краткое наименование клиента', max_length=250)
    Place = forms.CharField(label='Фактический адрес клиента', max_length=250)
    TaxNumber = forms.CharField(label='ИНН', max_length=100)
