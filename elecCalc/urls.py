from django.urls import path

from elecCalc.views import MainPage, DisplayCableView, DisplayDevicesView, DisplayReceiverView, \
    DisplayGroupReceiverView, EditCableView

app_name = 'elecCalc'

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('display-cable/', DisplayCableView.as_view(), name='display-cable'),
    path('display-device/', DisplayDevicesView.as_view(), name='display-device'),
    path('display-receiver/', DisplayReceiverView.as_view(), name='display-receiver'),
    path('display-group-receiver/', DisplayGroupReceiverView.as_view(), name='display-group-receiver'),
    path('edit-cable/<int:cable_id>/', EditCableView.as_view(), name='edit-cable'),
]