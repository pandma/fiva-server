from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ..models.Contact_User import Constact_User
import json


class Contact_user_views(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        comp = list(Constact_User.objects.values())
        if len(comp) > 0:
            data = {'message': "Success", 'Users': comp}
        else:
            data = {"message": "success", "Users": "not found"}
        return JsonResponse(data)

    def post(self, request):
        jd = json.loads((request.body))
        Constact_User.objects.create(
            name=jd['name'],
            email=jd['email'],
            phone=jd['phone'],
            product=jd['product'],
            message=jd['message']
        )
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request):
        jd = json.loads(request.body)
        query = jd['name']
        comp = list(Constact_User.objects.filter(name=query).values())
        comp_id = comp[0]['id']
        if len(comp) > 0:
            one_comp = Constact_User.objects.get(id=comp_id)
            one_comp.state = 'Processed'
            one_comp.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Users not found..."}
        return JsonResponse(data)
