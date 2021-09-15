from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name ="index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] ="太郎"
        return ctxt
    
class AboutView(TemplateView):
    template_name ="about.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"]=123
        ctxt["achieves"]=[
            "HOKKAIDO学生アプリコンテストにてクリプトン・フューチャー・メディア賞を受賞"
        ]
        ctxt["skills"]=[
            "Python",
            "Java",
            "JavaScript",
            ]
        ctxt["exams"]=[
            "応用情報技術者試験",
            "基本情報技術者試験",
            "SEA/J 情報セキュリティ技術認定基礎",
            "Python3認定技術者試験",
            ]
        return ctxt
    
