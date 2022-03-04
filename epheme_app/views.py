from django.shortcuts import render
from .models import Video, Category
from django.views import generic

# Create your views here.
class VideoListView(generic.ListView):
    model = Video
    template_name = 'epheme_app/index.html'
    context_object_name = 'video_list'
    paginate_by = 10
    
    def get_queryset(self):
        return Video.objects.order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class VideoDetailView(generic.DetailView):
    model = Video
    template_name = 'epheme_app/video_player.html'
def contact(request):
    return render(request, 'epheme_app/contact.html')
class FilterListView(generic.ListView):
    model = Video
    template_name = 'epheme_app/index.html'
    context_object_name = 'video_list'
    paginate_by = 10
    
    def get_queryset(self):
        return Video.objects.filter(category_name__slug=self.kwargs['slug']).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context