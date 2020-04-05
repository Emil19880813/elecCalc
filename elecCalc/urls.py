from django.urls import path

from elecCalc.views import DisplayCableView, DisplayDevicesView, DisplayReceiverView, \
    EditCableView, EditDeviceView, EditReceiverView, DeleteCableView, \
    DeleteDeviceView, DeleteReceiverView, AddCableView, AddDeviceView, \
    AddReceiverView, MainPage, CableListView, CableIddView

app_name = 'elecCalc'

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('display-cable/', DisplayCableView.as_view(), name='display-cable'),
    path('display-device/', DisplayDevicesView.as_view(), name='display-device'),
    path('display-receiver/', DisplayReceiverView.as_view(), name='display-receiver'),
    path('edit-cable/<int:cable_id>/', EditCableView.as_view(), name='edit-cable'),
    path('edit-device/<int:device_id>/', EditDeviceView.as_view(), name='edit-device'),
    path('edit-receiver/<int:receiver_id>/', EditReceiverView.as_view(), name='edit-receiver'),
    path('delete-cable/<int:cable_id>/', DeleteCableView.as_view(), name='delete-cable'),
    path('delete-device/<int:device_id>/', DeleteDeviceView.as_view(), name='delete-device'),
    path('delete-receiver/<int:receiver_id>/', DeleteReceiverView.as_view(), name='delete-receiver'),
    path('add-cable/', AddCableView.as_view(), name='add-cable'),
    path('add-device/', AddDeviceView.as_view(), name='add-device'),
    path('add-receiver/', AddReceiverView.as_view(), name='add-receiver'),
    path('cable-list/', CableListView.as_view(), name='cable-list'),
    path('display-idd/', CableIddView.as_view(), name='display-idd'),
]