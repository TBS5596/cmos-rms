import json
from django.shortcuts import redirect, render
import requests

from django.contrib.auth import logout as logout_func
from django.contrib.auth.decorators import login_required

from portal.forms import RiskForm, UpdateRiskMPForm

# api host link
host_url = 'http://127.0.0.1:8000/'

def view_dashboard(request):
    # get the top 10 risks based on their score
    risks = requests.get(f'{host_url}api/risks/top10')
    if risks.status_code == 200: # successful
        top_10_risks = risks.json() # convert text to json objects
    else:
        top_10_risks = {}
    # get other risk stats and convert to json objects then into a list for the chart
    risks_impact_stats = requests.get(f'{host_url}api/risks/impactStats')
    impact_stats = dataset(json.loads(risks_impact_stats.text))
    risks_likelihood_stats = requests.get(f'{host_url}api/risks/likelikehoodStats')
    likelihood_stats = dataset(json.loads(risks_likelihood_stats.text))
    risks_status_stats = requests.get(f'{host_url}api/risks/statusStats')
    status_stats = dataset(json.loads(risks_status_stats.text))
    # bandle all information needed for the fronend
    context = {
        'risks': top_10_risks,
        'risksImpactStats': impact_stats,
        'risksLikelihoodStats': likelihood_stats,
        'risksStatusStats': status_stats,
        }
    print(context)
    return render(request, 'portal/risk_dash.html', context)

def view_all_risks(request):
    # get all risks from api endpoint
    risks = requests.get(f'{host_url}api/risks')
    if risks.status_code == 200: # successful
        all_risks = risks.json() # convert text to json objects
    else:
        all_risks = {}
    return render(request, 'portal/risk_table.html', {'risks': all_risks})

def add_risk(request):
    # check the method used for the request
    if request.method == 'POST':
        form = RiskForm(request.POST) # bind the request data to a form object
        if form.is_valid(): # validate the form
            data = {
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'category': form.cleaned_data['category'],
                'owner': form.cleaned_data['owner'],
                'likelihood': form.cleaned_data['likelihood'],
                'impact': form.cleaned_data['impact'],
                'overall_score': form.cleaned_data['overall_score'],
                'status': form.cleaned_data['status'],
                'mitigation_plan': form.cleaned_data['mitigation_plan'],
                'review_date': form.cleaned_data['review_date'].isoformat()
            } # create a json object
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f'{host_url}api/risk/add', json=data, headers=headers) # post the data to the api endpoint
            if response.status_code == 200: # successful
                return redirect('all-risks')
            else: # unsuccessful
                error = f"Something went wrong!\n{response.text}"
                return render(request, 'portal/risk_form.html', {'form': form, 'error': error})
    else: # if it's a get request, return an empty form
       form = RiskForm()
    return render(request, 'portal/risk_form.html', {'form': form})

def view_risk(request, pk):
    risk = requests.get(f'{host_url}api/risk/{pk}')
    error = None
    if risk.status_code == 200:
        risk_to_view = risk.json()
    else:
        error = f"Something went wrong while trying to retrieve the risk!\n{risk.text}"
    return render(request, 'portal/risk_view.html', {'error': error, 'risk': risk_to_view})

def update_risk(request, pk):
    error = None
    if request.method == "GET":
        if pk is not None:
            risk = requests.get(f'{host_url}api/risk/{pk}')
            form = UpdateRiskMPForm()
            if risk.status_code == 200:
                risk_to_view = risk.json()
                return render(request, 'portal/risk_update.html', {'form': form, 'risk': risk_to_view})
            else:
                error = f"Something went wrong while trying to retrieve the risk!\n{risk.text}"
                return render(request, 'portal/risk_view.html', {'error': error, 'risk': risk_to_view})
    if request.method == 'POST':
        form = UpdateRiskMPForm(request.POST)
        if form.is_valid(): # validate the form
            data = {
                'owner': form.cleaned_data['owner'],
                'likelihood': form.cleaned_data['likelihood'],
                'impact': form.cleaned_data['impact'],
                'status': form.cleaned_data['status'],
                'mitigation_plan': form.cleaned_data['mitigation_plan']
            } # create a json object
            headers = {'Content-Type': 'application/json'}
            response = requests.put(f'{host_url}api/risk/add', json=data, headers=headers) # update the data to the api endpoint
            if response.status_code == 200: # successful
                return redirect('view-risk', pk=pk)
            else: # unsuccessful
                error = f"Something went wrong!\n{response.text}"
                return render(request, 'portal/risk_view.html', {'form': form, 'error': error})

##############################################################################################################
# creates a dataset from a json object
def dataset(data):
    labels = []
    values = []
    for key, value in data.items():
        labels.append(key)
        values.append(value)
    return {"labels": labels, "data": values}
