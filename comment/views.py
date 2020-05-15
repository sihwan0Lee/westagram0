import json
from django.views import View
from django.http import JsonResponse
from .models import Comment

class CommentView(View):
	def post(self, request):
		data = json.loads(request.body)
		Comment(
			email		=	data['email'],
			comments	=	data['comments']
		).save()

		return JsonResponse({'message':'댓글을 썻구나!!'}, status=200)

	def get(self, request):
		return JsonResponse({'comments':list(Comment.objects.value())}, status=200)
