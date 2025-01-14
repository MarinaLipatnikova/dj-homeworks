from django.urls import path

from measurement.views import SensorList, SensorUpdateDelite, AddMeasurement, DetailInfo

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorList.as_view()),
    path('sensors/<int:pk>/', SensorUpdateDelite.as_view()),
    path('measurements/', AddMeasurement.as_view()),
    path('sensors/info/<int:pk>/', DetailInfo.as_view())
]
