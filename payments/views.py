import stripe
from django.shortcuts import render
import stripe
# Create your views here.
from django.views.generic.base import TemplateView
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentPageView(TemplateView):
    template_name = 'pay_patient.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':

        doc = request.POST.get('doctor', '')
        print(doc)
        charge = stripe.Charge.create(
            amount=200000,
            currency='PKR',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
