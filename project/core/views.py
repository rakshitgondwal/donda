from django.shortcuts import render
from django.http import HttpResponse
from . import utils



def switch_view(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')

        if action == 'total':
            # Handle the 'total' action
            result = utils.count_records
        elif action == 'mean':
            # Handle the 'mean' action
            result = utils.find_mean
        elif action == 'median':
            # Handle the 'median' action
            result = utils.median
        elif action == 'p25':
            # Handle the 'p25' action
            result = utils.percentile_25
        elif action == 'p75':
            # Handle the 'p75' action
            result = utils.percentile_75
        else:
            # Handle the default case or show an error message
            result = "Unknown action"

        # Render a response, passing the result to the template
        return render(request, 'result_template.html', {'result': result})

    # Render the initial form
    return render(request, 'form_template.html')


def index(request):
    context = {'result' : result}
    return render(request, "file path" , context)