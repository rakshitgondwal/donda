from django.urls import path

from . import views, analysis


urlpatterns = [
    path("", views.upload_data, name="upload_data"),
    path("total/", analysis.count_records, name="upload_data"),
    path("mean/", analysis.find_mean, name="upload_data"),
    path("median/", analysis.median, name="upload_data"),
    path("p25/", analysis.percentile_25, name="upload_data"),
    path("p75/", analysis.percentile_75, name="upload_data"),
]