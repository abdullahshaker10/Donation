from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Example logic to fetch unread notifications
        context['unread_notifications'] = 3  # Replace with dynamic logic
        return context