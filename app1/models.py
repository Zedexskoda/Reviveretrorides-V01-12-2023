from django.db import models

class Car(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Model(models.Model):
    id=models.AutoField(primary_key=True)
    models = models.CharField(max_length=100)
    def __str__(self):
        return self.models
    

class All_Detail(models.Model):
    registration_no=models.CharField(max_length=50,primary_key=True)
    year = models.IntegerField()
    car=models.ForeignKey(Car, on_delete=models.CASCADE)
    car_model=models.ForeignKey(Model, on_delete=models.CASCADE)
    chassis_no = models.CharField(max_length=100)
    engine_no = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    manufacturing_year = models.IntegerField()
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.registration_no


class Work(models.Model):
    id=models.AutoField(primary_key=True)
    work=models.CharField(max_length=50)
    def __str__(self):
        return self.work


class car_x_mod(models.Model):
    car=models.ForeignKey(All_Detail, on_delete=models.CASCADE)
    work=models.ForeignKey(Work, on_delete=models.CASCADE)
    before_work=models.FileField(upload_to='before work/', max_length=100)
    estimate=models.IntegerField()
    remarks=models.TextField()




class final_settlement(models.Model):
    car=models.ForeignKey(All_Detail, on_delete=models.CASCADE)
    work=models.ForeignKey(Work, on_delete=models.CASCADE)
    after_work=models.FileField(upload_to='after work/', max_length=100)
    estimate=models.IntegerField()
    Final_cost=models.IntegerField()
    remarks=models.TextField()


