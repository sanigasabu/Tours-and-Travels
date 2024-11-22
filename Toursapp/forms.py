from django import forms
from.models import *

class TraveluserForm(forms.ModelForm):
    class Meta:
        model = Traveluser
        fields = ['Name','whatsap_no']

class Loginform(forms.Form):
    username =forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ['duration']  # Exclude the duration field from the form
        widgets = {
            'departure_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class PackagePlaceForm(forms.ModelForm):
    class Meta:
        model = Package_place
        fields = ['place_name', 'image','description']

class PackageDetailsForm(forms.ModelForm):
    class Meta:
        model=Package_detail
        fields = '__all__'


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'place','description','hotel_type','image','inclusion']


class TourDayPlannerForm(forms.ModelForm):
    class Meta:
        model = TourDayPlanner
        fields = '__all__'


class UserBookingForm(forms.ModelForm):
    class Meta:
        model = UserBooking
        fields = [ 'passenger_name', 'passenger_email', 'contact_info', 'passport_number']

    def __init__(self, *args, **kwargs):
        super(UserBookingForm, self).__init__(*args, **kwargs)

class memberaccountForm(forms.ModelForm):
    class Meta:
        model= memberaccount
        fields= '__all__'


class MemberAccountForm1(forms.ModelForm):
    class Meta:
        model = memberaccount
        fields = ['amount']

class Locationform(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['country','package']
