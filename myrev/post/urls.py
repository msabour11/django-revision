from django.urls  import reverse ,path,include
from post.views import CreateView,ListPost,UpdatePost,DeletePost,ShowPost


urlpatterns =[
    path('create/',CreateView.as_view(),name='post.create'),
    path('list/',ListPost.as_view(),name='post.list'),
    path('<int:pk>/edit',UpdatePost.as_view(),name='post.edit'),
    path('<int:pk>/delete',DeletePost.as_view(),name='post.delete'),
    path('<int:pk>/show',ShowPost.as_view(),name='post.show'),




    
]