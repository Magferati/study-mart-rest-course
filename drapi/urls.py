from django.urls import path
from .views import aiquest_info , aiquest_inst,aiquest_create

urlpatterns = [
    path('ai-info/',aiquest_info),
    path('ai-inst/<int:pk>/',aiquest_inst),
    path('aicreate/', aiquest_create),
]