import datetime
from django.shortcuts import render, redirect
from django.views.generic import View
from docxtpl import DocxTemplate
from .forms import MainForm
from docx2pdf import convert
import comtypes.client


# Create your views here.
class ProductForm(View):

    def doc_form(request):
        if request.method == 'POST':
            form = MainForm(request.POST)
            if form.is_valid():
                form.clean()
                clean = form.cleaned_data
                time_now = int(datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).timestamp())
                name = 'complete_' + str(time_now)
                temp_name = ['template_1', 'template_2']
                for i in temp_name:
                    doc = DocxTemplate('doc/doc_template/' + i + '.docx')
                    context = clean
                    doc.render(context)
                    doc.save('doc/doc_complete/' + name + i + '.docx')
                    comtypes.CoInitializeEx(0)
                    convert('doc/doc_complete/' + name + i + '.docx', 'doc/doc_complete/' + name + i + '.pdf')
                return redirect('/')
            else:
                pass
        else:
            form = MainForm()

        return render(request, 'doc/index.html', {'form': form})
