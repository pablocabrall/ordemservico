from django.shortcuts import render

def ordem_servico_list(request):
    template_name = 'servico/ordem_servico_list.html'
    #object_list = OrdemServico.objects.all()
    #context = {
    #    'object_list': object_list
    #}

    return render(request, template_name)
