from django.shortcuts import render, redirect
from django.http import HttpResponse
from calculator_python import calculator

def calculator_view(request):
    if request.method == 'POST':
        form = calculator(request.POST)
        if form.is_valid():
            consumption = [
                form.cleaned_data['month1'],
                form.cleaned_data['month2'],
                form.cleaned_data['month3'],
            ]
            distributor_tax = form.cleaned_data['distributor_tax']
            tax_type = form.cleaned_data['tax_type']

            annual_savings, monthly_savings, applied_discount, coverage = calculator(
                consumption, distributor_tax, tax_type
            )

            return render(request, 'calculator_form.html', {
                'form': form,
                'annual_savings': annual_savings,
                'monthly_savings': monthly_savings,
                'applied_discount': applied_discount,
                'coverage': coverage,
            })
    

    return render(request, 'calculator_form.html')
