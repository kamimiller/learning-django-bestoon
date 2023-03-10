from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from web.models import User, Token, Expense, Income
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_income(request):
    """user submits an income"""

    #TODO: validate data. user might be fake, token might be fake, amount might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'data' not in request.POST:
        date = datetime.now()
    Income.objects.create(user=this_user,amount=request.POST['amount'],text=request.POST['text'], date=date)
    return JsonResponse(
        {
            'status':'ok',
        },encoder=JSONEncoder
    )
    
@csrf_exempt
def submit_expense(request):
    """user submits an expense"""

    #TODO: validate data. user might be fake, token might be fake, amount might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'data' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user=this_user,amount=request.POST['amount'],text=request.POST['text'], date=date)
    return JsonResponse(
        {
            'status':'ok',
        },encoder=JSONEncoder
    )