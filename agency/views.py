from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"
# 自分で定義したIndexViewに引数でgenericのTenplateViewクラスを渡している。
# as_view()メソッドはTemplateViewクラス内で定義されている。