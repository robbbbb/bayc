from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.landing_page_view, name="landing_page_view"),
    path('transaction_events/', views.transfer_events_view, name="transfer_events_view"),

    # API Endpoints
    path('api/v1/transfer_events/', api.TransferEventsView.as_view(), name="transfer_events"),
    path('api/v1/transfer_events/<int:token_id>/', api.TransferEventDetailView.as_view(),
         name="transfer_event_detail"),
]
