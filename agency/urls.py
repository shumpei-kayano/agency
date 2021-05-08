from django.urls import path

from.import views

app_name = 'agency'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    # 問い合わせページinquiry.htmlへのパス
    path('inquiry',views.InquiryView.as_view(),name="inquiry"),
    path('team',views.TeamView.as_view(),name="team"),
]
