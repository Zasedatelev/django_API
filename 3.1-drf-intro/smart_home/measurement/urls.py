from django.urls import path
from measurement.views import APISensorList, APISensorRetrieve, APISensorCreate,APISensorUpdate, APISensorMeasurement
urlpatterns = [
    path('api/sensors/', APISensorCreate.as_view()),
    path('api/sensors/', APISensorUpdate.as_view()),
    path('api/sensors/', APISensorMeasurement.as_view()),
    path('api/sensors/', APISensorList.as_view()),
    path('api/sensors/', APISensorRetrieve.as_view())

]
