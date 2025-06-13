from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class TruckLocation(models.Model):
    truck_number = models.CharField(max_length=50, null=True, blank=True)
    driver_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.truck_number} - {self.driver_name}"

class Stations(models.Model):
    tracking = models.ForeignKey(TruckLocation, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    check_in = models.CharField(max_length=50, null=True, blank=True)
    check_out = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class PlantMaster(models.Model):
    plant_name = models.CharField(max_length=100, null=True, blank=True)
    plant_address = models.CharField(max_length=255, null=True, blank=True)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.plant_name

class TruckTransactionMaster(models.Model):
    truck_no = models.CharField(max_length=50, null=True, blank=True)
    transaction_date = models.DateField(null=True)
    city_name = models.CharField(max_length=100, null=True, blank=True)
    transporter = models.CharField(max_length=100, null=True, blank=True)
    amount_per_ton = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    deliver_point = models.CharField(max_length=100, null=True, blank=True)
    truck_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.truck_no} - {self.transaction_date}"

class TruckTransactionDetails(models.Model):
    transaction = models.ForeignKey(TruckTransactionMaster, on_delete=models.CASCADE, null=True)
    plant = models.ForeignKey(PlantMaster, on_delete=models.CASCADE, null=True)
    loading_slip_no = models.CharField(max_length=100, null=True, blank=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    priority = models.CharField(max_length=50, null=True, blank=True)
    freight = models.CharField(max_length=50, null=True, blank=True)
    check_in_status = models.IntegerField(default=0)
    check_out_status = models.IntegerField(default=0)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.loading_slip_no or "Detail"

class TruckTransactions(models.Model):
    truck_no = models.CharField(max_length=50)
    transaction_date = models.DateField()
    city_name = models.CharField(max_length=100)
    transporter = models.CharField(max_length=100)
    amount_per_ton = models.DecimalField(max_digits=10, decimal_places=2)
    truck_weight = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_point = models.CharField(max_length=200)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    check_in_status = models.IntegerField(default=0)
    check_out_status = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.truck_no} - {self.transaction_date}"

class LoadingMaster(models.Model):
    transporter_name = models.CharField(max_length=100, null=True, blank=True)
    truck_no = models.CharField(max_length=50, null=True, blank=True)
    driver_name = models.CharField(max_length=100, null=True, blank=True)
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.truck_no or "LoadingMaster"

class LoadingShiftingDetails(models.Model):
    loading = models.ForeignKey(LoadingMaster, on_delete=models.CASCADE, null=True)
    driver_name = models.CharField(max_length=100, null=True, blank=True)
    plant_name = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.driver_name} - {self.plant_name}"

class LoadingDetails(models.Model):
    transaction = models.ForeignKey(TruckTransactions, on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=100, null=True, blank=True)
    loading_slip_no = models.CharField(max_length=50, null=True, blank=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    priority = models.IntegerField(null=True)
    freight = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.loading_slip_no or "LoadingDetail"

class TransportMaster(models.Model):
    transporter_name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.transporter_name
