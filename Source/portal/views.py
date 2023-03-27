from django.shortcuts import redirect, render
import requests

from portal.forms import RiskForm

# api host link
host_url = 'http://127.0.0.1:8000/'

def view_all_risks(request):
    # get all risks from api endpoint
    risks = requests.get(f'{host_url}api/risks')
    if risks.status_code == 200:
        all_risks = risks.json()
    else:
        all_risks = {}
    return render(request, 'portal/all_risks.html', {'risks': all_risks})

def add_risk(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            data = {}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f'{host_url}api/risk/add', json=data, headers=headers)
            if response.status_code == 200:
                return redirect('all-risks')
            else:
                error = ""
                return render(request, 'portal/add_risk.html', {'form': form, 'error': error})
    else:
       form = RiskForm()
    return render(request, 'portal/add_risk.html', {'form': form})