from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ..models.Maximeter_50_plus import Maximeter_50_plus
import json


class Maximeter_50_plusViews(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        max = list(Maximeter_50_plus.objects.values())
        if len(max) > 0:
            data = {'message': "Success", 'maximeters': max}
        else:
            data = {"message": "success", "maximeters": "not found"}
        return JsonResponse(data)

    def post(self, request):
        jd = json.loads((request.body))
        Maximeter_50_plus.objects.create(
            owner=jd['owner'],
            direction=jd['direction'],
            postalcode=jd['postalcode'],
            cups=jd['cups'],
            nif=jd['nif'],
            quarter_hour_curve=jd['quarter_hour_curve'],
            hired_power=jd['hired_power']
        )
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        maxs = list(Maximeter_50_plus.objects.filter(id=id).values())
        if len(maxs) > 0:
            max = Maximeter_50_plus.objects.get(id=id)
            max.anualConsumption = jd['anualConsumption']
            max.annualSavings = jd['annualSavings']
            max.recomendedPower = jd['recomendedPower']
            max.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Company not found..."}
        return JsonResponse(data)
