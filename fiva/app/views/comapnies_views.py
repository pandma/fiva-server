from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ..models.Company import Company
import json


class companies_views(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        comp = list(Company.objects.values())
        if len(comp) > 0:
            data = {'message': "Success", 'Copanies': comp}
        else:
            data = {"message": "success", "Copanies": "not found"}
        return JsonResponse(data)

    def post(self, request):
        jd = json.loads((request.body))
        Company.objects.create(
            name=jd['name'],
            p1=jd['p1'],
            p2=jd['p2'],
            p3=jd['p3'],
            p4=jd['p4'],
            p5=jd['p5'],
            p6=jd['p6']
        )
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request):
        jd = json.loads(request.body)
        query = jd['name']
        comp = list(Company.objects.filter(name=query).values())
        print("######",  query)
        comp_id = comp[0]['id']
        if len(comp) > 0:
            one_comp = Company.objects.get(id=comp_id)
            one_comp.p1 = jd['p1']
            one_comp.p2 = jd['p2']
            one_comp.p3 = jd['p3']
            one_comp.p4 = jd['p4']
            one_comp.p5 = jd['p5']
            one_comp.p6 = jd['p6']
            one_comp.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Company not found..."}
        return JsonResponse(data)
