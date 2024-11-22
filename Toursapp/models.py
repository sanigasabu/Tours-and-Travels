from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USER_TYPE_CHOICES = [
        ('ADMIN ', 'Admin '),
        ('USER ', 'user'),
    ]
STATUS_CHOICE=(
("ACTIVE","Active"),
("DEACTIVE","Deactive"),
)

class Userprofile(AbstractUser):
    # username
    # password
    # email
    contactno=models.CharField(max_length=10,null=False,blank=False)
    user_type=models.CharField(
        max_length=50,null=False,blank=False,choices=USER_TYPE_CHOICES
    )
    is_active = models.BooleanField(null=False,blank=True,default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    def _str_(self):
        return str(self.username)

class TravelAdmin(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    traveladmin=models.OneToOneField(
        Userprofile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    address=models.TextField(max_length=100,default=True,null=True)
    status=models.CharField(default="Active",max_length=50)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    def _str_(self):
        return str(self.Name)

class Traveluser(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    traveluser=models.OneToOneField(
        Userprofile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    whatsap_no=models.CharField(max_length=10,null=False,blank=False)
    status = models.CharField(default="Active",max_length=50)
    is_active = models.BooleanField(null=False, blank=True, default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    def _str_(self):
        return str(self.Name)

class Flight(models.Model):
    flight_no=models.CharField(max_length=250)
    departure_city=models.CharField(max_length=250)
    arrival_city=models.CharField(max_length=250)
    departure_date=models.DateTimeField()
    arrival_date=models.DateTimeField()
    duration=models.DurationField()
    tickate_rate=models.DecimalField(max_digits=10,decimal_places=2)
    airline=models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if self.departure_date and self.arrival_date:
            self.duration = self.arrival_date - self.departure_date
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.flight_no)

class Hotel(models.Model):
    HOTEL_CHOICES = [
        ('3 star ', '3 Star '),
        ('4 star ', '4 Star '),
        ('5 star ', '5 Star'),
        # Add more choices as needed
    ]
    name = models.CharField(max_length=250)
    place=models.CharField(max_length=250)
    description = models.TextField()
    hotel_type=models.CharField(max_length=250, choices=HOTEL_CHOICES)
    image = models.ImageField(upload_to='images')
    inclusion=models.CharField(max_length=250)
    def __str__(self):
        return str(self.name)

class Package_place(models.Model):
    id=models.AutoField(primary_key=True)
    place_name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images')
    description=models.TextField()
    def __str__(self):
        return str(self.place_name)

class Package_detail(models.Model):
    PACKAGE_CHOICES = [
        ('silver ', 'Silver '),
        ('gold ', 'Gold '),
        ('bronze ', 'Bronze'),
        # Add more choices as needed
    ]
    DAY_CHOICES = [
        ('three days ', 'Three Days '),
        ('five days ', 'Five Days '),
        ('seven days ', 'Seven Days'),
        ]
    id=models.AutoField(primary_key=True)
    package_name=models.CharField(max_length=250)
    place= models.ForeignKey(Package_place,on_delete=models.CASCADE)
    package_type=models.CharField(max_length=250, choices=PACKAGE_CHOICES)
    description=models.TextField()
    image = models.ImageField(upload_to='images')
    total_days=models.CharField(max_length=250, choices=DAY_CHOICES)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    go_flights = models.ManyToManyField(Flight, related_name='go_flights')
    return_flights = models.ManyToManyField(Flight, related_name='return_flights')
    inclusion=models.CharField(max_length=250)
    def __str__(self):
        return str(self.package_name)


class TourDayPlanner(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package_detail, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    day_number = models.PositiveIntegerField()
    breakfast = models.ForeignKey(Hotel, related_name='breakfast', on_delete=models.SET_NULL, null=True, blank=True)
    lunch = models.ForeignKey(Hotel, related_name='lunch', on_delete=models.SET_NULL, null=True, blank=True)
    visiting_place = models.TextField()
    dinner = models.ForeignKey(Hotel, related_name='dinner', on_delete=models.SET_NULL, null=True, blank=True)
    details = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.package)

class UserBooking(models.Model):
    id= models.AutoField(primary_key=True)
    package = models.ForeignKey(Package_detail, to_field='id', on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    contact_info = models.CharField(max_length=15)
    passport_number=models.CharField(max_length=20)
    userid=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.passenger_name)

class memberaccount(models.Model):
    id=models.AutoField(primary_key=True)
    account_number=models.CharField(max_length=50)
    IFSC=models.CharField(max_length=50)
    key=models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    member = models.ForeignKey(
        Userprofile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return str(self.member)

class Location(models.Model):
    country=models.ForeignKey(Package_place,on_delete=models.CASCADE)
    package=models.ForeignKey(Package_detail,on_delete=models.CASCADE)
    place_name=models.CharField(max_length=45,null=True,blank=True)
    latitude = models.DecimalField(max_digits=30,decimal_places=20,null=True,blank=True)
    longitude = models.DecimalField(max_digits=30,decimal_places=20,null=True,blank=True)
    def __str__(self):
        return str(self.place_name)






