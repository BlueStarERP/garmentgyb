from django.db import models

# Create your models here.
class groupmodel(models.Model):
    groupname = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.groupname

class department(models.Model):
    group_name = models.ForeignKey(groupmodel, on_delete=models.CASCADE, blank=True)
    department_name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

class gender(models.Model):
    gendertype = models.CharField(max_length=20)

    def __str__(self):
        return self.gendertype

class region(models.Model):
    region_name = models.CharField(max_length=20)

    def __str__(self):
        return self.region_name

class employee(models.Model):
    photo = models.ImageField(upload_to='emp', blank=True, null=True)
    employee_code = models.CharField(max_length=225)
    employee_eng_name = models.CharField(max_length=225)
    employee_mm_name = models.CharField(max_length=225)
    group_name = models.ForeignKey(groupmodel, on_delete=models.CASCADE, blank=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE, blank=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    point = models.CharField(max_length=255, blank=True, null=True)

    nrc_no = models.CharField(max_length=225)
    ssb_no = models.CharField(max_length=225, blank=True, null=True)
    mobile = models.CharField(max_length=225, blank=True, null=True)
    gender = models.CharField(max_length=225)
    region = models.ForeignKey(region, on_delete=models.CASCADE, blank=True)
    address = models.TextField()

    resign = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_eng_name

