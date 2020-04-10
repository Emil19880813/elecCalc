from django.urls import path

from elecCalc.views import DisplayCableView, DisplayDevicesView, \
    EditCableView, EditDeviceView, DeleteCableView, \
    DeleteDeviceView, AddCableView, AddDeviceView, \
    MainPage, CableListView, CableIddView, export_to_csv, DeleteResultView, PositionChange

app_name = 'elecCalc'

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('display-cable/', DisplayCableView.as_view(), name='display-cable'),
    path('display-device/', DisplayDevicesView.as_view(), name='display-device'),
    path('edit-cable/<int:cable_id>/', EditCableView.as_view(), name='edit-cable'),
    path('edit-device/<int:device_id>/', EditDeviceView.as_view(), name='edit-device'),
    path('delete-cable/<int:cable_id>/', DeleteCableView.as_view(), name='delete-cable'),
    path('delete-device/<int:device_id>/', DeleteDeviceView.as_view(), name='delete-device'),
    path('delete-cable-list/<int:result_id>/', DeleteResultView.as_view(), name='delete-result'),
    path('add-cable/', AddCableView.as_view(), name='add-cable'),
    path('add-device/', AddDeviceView.as_view(), name='add-device'),
    path('cable-list/', CableListView.as_view(), name='cable-list'),
    path('display-idd/', CableIddView.as_view(), name='display-idd'),
    path('/position/', PositionChange.as_view(), name='position'),
    path('export-to-csv/', export_to_csv, name='csv'),
]