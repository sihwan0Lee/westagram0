import json

from django.views import View
from django.http import JsonResponse

from .models import Comment
from core.utils import login_decorator

class CommentView(View):
	@login_decorator
	def post(self, request):
		data = json.loads(request.body)
		Comment(
			email		=	request.user.email,
			comments	=	data['comments']
		).save()

		return JsonResponse({'comments':list(Comment.objects.values())}, status=200)

	@login_decorator
	def get(self, request):
		print(Comment.objects.values())
		
		return JsonResponse({'comments':list(Comment.objects.values())}, status=200)
