from django.urls import path
from .views	import CommentView


urlpatterns = [
	path('ent', CommentView.as_view()),
]
