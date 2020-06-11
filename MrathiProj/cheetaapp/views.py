from django.shortcuts import render, redirect, HttpResponse
from django import forms
from .models import Card

# Create your views here.


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'


def make_card(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
            # return HttpResponse('card created successfully')
    return render(request, 'card_form.html', {'form':form})


def data_card(request):
    cards = Card.objects.all()

    return render(request, 'card_list.html', {'cards':cards})


# import subprocess
# from PIL import Image

# def image_as_png_pdf(request):
#   output_format = request.GET.get('format')
#   im = Image.open(path_to_image) # any Image object should work
#   if output_format == 'png':
#     response = HttpResponse(mimetype='image/png')
#     response['Content-Disposition'] = 'attachment; filename=%s.png' % filename
#     im.save(response, 'png') # will call response.write()
#   else:
#     # Temporary disk space, server process needs write access
#     tmp_path = '/tmp/'
#     # Full path to ImageMagick convert binary
#     convert_bin = '/usr/bin/convert' 
#     im.save(tmp_path+filename+'.png', 'png')
#     response = HttpResponse(mimetype='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
#     ret = subprocess.Popen([ convert_bin, 
#                             "%s%s.png"%(tmp_path,filename), "pdf:-" ],
#                             stdout=subprocess.PIPE)
#     response.write(ret.stdout.read())
#   return response