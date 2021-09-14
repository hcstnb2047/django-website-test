from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name ="index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] ="tanabe"
        return ctxt
    
class AboutView(TemplateView):
    template_name ="about.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"]=123
        ctxt["skills"]=[
            "Python",
            "C++",
            "JavaScript",
            ]
        return ctxt
    