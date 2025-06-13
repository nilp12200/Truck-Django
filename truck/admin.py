from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(TruckLocation)
admin.site.register(Stations)
admin.site.register(PlantMaster)
admin.site.register(TruckTransactionMaster)
admin.site.register(TruckTransactionDetails)
admin.site.register(TruckTransactions)
admin.site.register(LoadingMaster)
admin.site.register(LoadingShiftingDetails)
admin.site.register(LoadingDetails)
admin.site.register(TransportMaster)
