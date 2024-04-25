

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Posts
from .filters import PostsFilter


class PostsList(ListView):
    model = Posts
    ordering = '-name_post'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostsFilter(self.request.GET, queryset)
       return self.filterset.qs

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context


class PostDetail(DetailView):

    model = Posts

    template_name = 'post.html'

    context_object_name = 'post'

