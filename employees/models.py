from django.db import models

class Name(models.Model):
    employee_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    role = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=15)
    hire_date = models.DateField()
    is_currently_working = models.BooleanField(default=True)

    def __str__(self):
        return f"({self.employee_id}) - {self.first_name} {self.last_name}, {self.role} , {self.hire_date}"