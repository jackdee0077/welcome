from django.contrib import admin
from django.urls import path

from squaring.views import squaringView,HelloworldView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:number>', squaringView.as_view(), name='home'),
    path("hello/<name>",HelloworldView.as_view())
]