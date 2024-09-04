from django.shortcuts import render, redirect
from calculator_python import Consumer

def calculator(request):
    if request.method == 'POST':
        consumption = Consumer(
            name=request.POST['name'],
            document=request.POST['document'],
            zip_code=request.POST['zip_code'],
            city=request.POST['city'],
            state=request.POST['state'],
            consumption=request.POST['consumption'],
            distributor_tax=request.POST['distributor_tax'],
            tariff_type=request.POST['tariff_type'],
        )
        consumption.save()
        results = consumption.calculate_savings_and_coverage()
        return render(request, 'calculator.html', {'results': results})
    else:
        return render(request, 'calculator.html')

def view1(request):
    consumers = Consumer.objects.all()
    data = []
    for consumer in consumers:
        savings_and_coverage = consumer.calculate_savings_and_coverage()
        data.append({
            'consumer': consumer,
            'savings_and_coverage': savings_and_coverage,
        })
    return render(request, 'consumers.html', {'data': data})

def view2(request):
    if request.method == 'POST':
        consumer = Consumer(
            name=request.POST['name'],
            document=request.POST['document'],
            zip_code=request.POST['zip_code'],
            city=request.POST['city'],
            state=request.POST['state'],
            consumption=request.POST['consumption'],
            distributor_tax=request.POST['distributor_tax'],
            tariff_type=request.POST['tariff_type'],
        )
        consumer.save()
        return redirect('view1')
    else:
        return render(request, 'create_consumer.html')