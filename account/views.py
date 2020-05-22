import json
import bcrypt
import jwt

from westagram.settings import SECRET_KEY
from .models import Account

from django.views import View
from django.http import JsonResponse, HttpResponse

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email = data['email']).exists():
                return JsonResponse({"message":"EMAIL_ALREADY_EXIST"},status=400)

            

                             
            password_crypt = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()) 
            password_crypt = password_crypt.decode('utf-8')            

           

            Account(
                email    = data['email'],
				username = data['username'],
				fullname = data['fullname'],
                password = password_crypt                          
            ).save()

            return JsonResponse({"message":"SUCCESS"},status=200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email = data['email']).exists() :
                user = Account.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) :
                
                    

                    token = jwt.encode({'email' : data['email']}, SECRET_KEY, algorithm = "HS256")
                    token = token.decode('utf-8')   

                    
                    return JsonResponse({"token" : token }, status=200)

                else :
                    return JsonResponse({"message":"WRONG_ID_OR_PASSWORD"},status=401)

            return JsonResponse({"message":"WRONG_ID_OR_PASSWORD"},status=401)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 401)

class TokenCheckView(View):
    def post(self,request):
        data = json.loads(request.body)

        token_info = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')

        if Account.objects.filter(email=token_info['email']).exists() :
            return JsonResponse({"message":"SUCCESS"},status=200)

        return JsonResponse({"message":"INVALID_REQUEST"},status=400)
