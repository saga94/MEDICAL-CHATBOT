from django.db import models

# Create your models here.
class users(models.Model):
	name=models.CharField(max_length=159);
	email=models.CharField(max_length=159);
	pass_word=models.CharField(max_length=159);
	phone=models.CharField(max_length=159);
	city=models.CharField(max_length=159);
	gender=models.CharField(max_length=159);
	age=models.CharField(max_length=159);

class queries(models.Model):
    q_n=models.CharField(max_length=1000);
    an_s=models.CharField(max_length=1000);

class dataset(models.Model):
    Symptoms=models.CharField(max_length=500);
    Causes=models.CharField(max_length=500);
    Disease=models.CharField(max_length=500);
    Medicine=models.CharField(max_length=500);
    Specialist=models.CharField(max_length=500);



class chat(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	message=models.CharField(max_length=5000);


class docchat(models.Model):
    name=models.CharField(max_length=100);
    email=models.CharField(max_length=100);
    message=models.TextField();
    chatbw = models.CharField(max_length=100);
    stz = models.CharField(max_length=10);


class doctors(models.Model):
    Specialist=models.CharField(max_length=1000);
    email=models.CharField(max_length=100);
    name=models.CharField(max_length=100);
    qualification=models.CharField(max_length=100);
    contact=models.CharField(max_length=100);
    password=models.CharField(max_length=100);
    stz=models.CharField(max_length=100);


class performance(models.Model):
    alg_name = models.CharField(max_length=100)
    sc1 = models.FloatField()
    sc2 = models.FloatField()
    sc3 = models.FloatField()
    sc4 = models.FloatField()



    