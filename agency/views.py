from django.shortcuts import render
# genericの読み込みで使用できるようにする
from django.views import generic
# 問い合わせページInquiryFormの読み込み
from.forms import InquiryForm
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"
# 自分で定義したIndexViewに引数でgenericのTenplateViewクラスを渡している。
# as_view()メソッドはTemplateViewクラス内で定義されている。

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm