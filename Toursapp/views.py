from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login
from django.views import View
import random, json
from django.http import HttpResponse,JsonResponse

# Create your views here.
def generate_account_details(pk):
    accntnumber = ""
    key = ""
    ifsc = ""
    list_of_chars = "1234567890"
    accntnumber_length = 11
    key_length = 3

    for i in range(accntnumber_length):
        accntnumber += random.choice(list_of_chars)
    for i in range(key_length):
        key += random.choice(list_of_chars)

    ifsc = "SBTR000055"
    amt = "500000"

    account_details = {
        'account_number': accntnumber,
        'key': key,
        'IFSC': ifsc,
        'amount': amt,
        'member':pk,
    }
    return (account_details)

class user_registraction(View):

    def get(self, request):
        forms = TraveluserForm()
        return render(request, 'registraction.html', {'forms': forms})

    def post(self, request):
        forms = TraveluserForm(request.POST)
        if forms.is_valid():
            user_admin = forms.save(commit=False)
            travel_user = Userprofile.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    email=request.POST['email'],
                    contactno=request.POST['contactno'],
                    user_type='USER'
                )
            useraccount=generate_account_details(travel_user.id)
            member_account = memberaccount.objects.create(
                account_number=useraccount['account_number'],
                IFSC=useraccount['IFSC'],
                key=useraccount['key'],
                amount=useraccount['amount'],
                member_id=useraccount['member']
            )
            member_account.save()
            user_admin.traveluser = travel_user
            user_admin.save()
            return redirect('login')  # Redirect to login page after successful registration

def login_view(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['userid'] = user.id

                if user.is_staff:
                    return render(request, 'adminpanel.html')
                elif  user.is_authenticated:
                    return render(request, 'index.html')
    else:
        form = Loginform()

    return render(request,'login.html', {'form': form})

def home(request):
    return render(request,'index.html')

def history(request):
    user_id = request.session.get('userid')
    bookings = UserBooking.objects.filter(userid=user_id)
    return render(request, 'Bookinghistory.html', {'bookings': bookings})

def adminpanel(request):
    return render(request,'adminpanel.html')

def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_flights')
    else:
        form = FlightForm()
    return render(request, 'flightadd.html', {'form': form})

def manage_flights(request):
    flights = Flight.objects.all()
    return render(request, 'flightmanage.html', {'flights': flights})

def edit_flight(request,id):
    flight = Flight.objects.get(pk=id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('manage_flights')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flightedit.html', {'form': form})

def delete_flight(request,id):
    form=Flight.objects.get(pk=id)
    form.delete()
    return redirect('manage_flights')

def add_packageplace(request):
    if request.method == 'POST':
        form = PackagePlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_packageplace')  # Redirect to a success page
    else:
        form = PackagePlaceForm()
    return render(request, 'packageplaceadd.html', {'form': form})

def manage_packageplaces(request):
    packageplaces = Package_place.objects.all()
    return render(request, 'packageplacemanage.html', {'packageplaces': packageplaces})

def edit_packageplaces(request,id):
    packageplaces = Package_place.objects.get(pk=id)
    if request.method == 'POST':
        form = PackagePlaceForm(request.POST, instance=packageplaces)
        if form.is_valid():
            form.save()
            return redirect('manage_packageplace')
    else:
        form = PackagePlaceForm(instance=packageplaces)
    return render(request, 'packageplaceedit.html', {'form': form})

def delete_packageplaces(request,id):
    form=Package_place.objects.get(pk=id)
    form.delete()
    return redirect('manage_packageplace')

def add_packagedetails(request):
    if request.method == 'POST':
        form = PackageDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_packagedetails')
    else:
        form = PackageDetailsForm()
    return render(request, 'packagedetailsadd.html', {'form': form})

def manage_Packagedetails(request):
    packages = Package_detail.objects.all()
    return render(request, 'packagedetailsmanage.html', {'packages': packages})

def edit_Packagedetails(request,id):
    package = Package_detail.objects.get(pk=id)
    if request.method == 'POST':
        form = PackageDetailsForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('manage_packagedetails')
    else:
        form = PackageDetailsForm(instance=package)
    return render(request, 'packagedetailsedit.html', {'form': form})

def add_planner(request):
    if request.method == 'POST':
        form = TourDayPlannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_planner')  # Redirect to a success page
    else:
        form = TourDayPlannerForm()

    return render(request, 'dayplanneradd.html', {'form': form})

def manage_planner(request):
    planers = TourDayPlanner.objects.all()
    return render(request, 'dayplannermanage.html', {'planers': planers})

def edit_planner(request,id):
    planner = TourDayPlanner.objects.get(pk=id)
    if request.method == 'POST':
        form = TourDayPlannerForm(request.POST, instance=planner)
        if form.is_valid():
            form.save()
            return redirect('manage_planner')
    else:
        form = TourDayPlannerForm(instance=planner)
    return render(request, 'dayplanneredit.html', {'form': form})

def delete_planner(request,id):
    form=TourDayPlanner.objects.get(pk=id)
    form.delete()
    return redirect('manage_planner')

def delete_Packagedetails(request,id):
    form=Package_detail.objects.get(pk=id)
    form.delete()
    return redirect('manage_packagedetails')

def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_hotels')  # Redirect to a success page
    else:
        form = HotelForm()

    return render(request, 'hoteladd.html', {'form': form})

def manage_hotel(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotelmanage.html', {'hotels': hotels})

def edit_hotel(request,id):
    hotel = Hotel.objects.get(pk=id)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('manage_hotels')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hoteledit.html', {'form': form})

def delete_hotel(request,id):
    form=Hotel.objects.get(pk=id)
    form.delete()
    return redirect('manage_hotels')

def view_user_bookings(request):
    bookings = UserBooking.objects.all()
    return render(request, 'adminviewbooking.html', {'bookings': bookings})

def view_user(request):
    users = Userprofile.objects.all()  # Use the correct model
    return render(request, 'adminviewalluser.html', {'users': users})

def save_location(request):
    if request.method == 'GET':
        pack = Package_detail.objects.all()
        pla = Package_place.objects.all()
        return render(request, 'savelocation.html', {'pack':pack, 'pla': pla})
    elif request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        place_name = request.POST.get('place_name')
        country_id = request.POST.get('country')
        package_id = request.POST.get('package')
        country = get_object_or_404(Package_place, id=country_id)
        package = get_object_or_404(Package_detail, id=package_id)

        loc = Location.objects.create(
            latitude=latitude,
            longitude=longitude,
            place_name=place_name,
            country=country,
            package=package
        )
    return redirect('admin_panel')


def user_packageplaceview(request):
    packageplaces = Package_place.objects.all()
    return render(request, 'userviewpackageplace.html', {'packageplaces': packageplaces})

def user_packageview(request,pk):
    package_detail = Package_detail.objects.filter(place=pk)
    return render(request, 'userviewpackage.html', {'package_detail': package_detail,'packageplaceid':pk})

def user_plannerview(request,pk,packageplaceid):
    planers = TourDayPlanner.objects.filter(package=pk)
    pk2=packageplaceid
    return render(request, 'userviewdayplanner.html', {'planers': planers,'packageid':pk,'packageplaceid':pk2})

def package_booking(request,packageid,packageplaceid):
    packageplace = Package_place.objects.filter(id=packageplaceid).first()
    packageid1=packageid
    if packageplace:
        placename = packageplace.place_name
        package = Package_detail.objects.filter(id=packageid).first()
    if package:
        packagename = package.package_name
        packagetype = package.package_type
        packageamount=package.total_amount
    user_id = request.session.get('userid')
    accountdetails=memberaccount.objects.filter(member=user_id).first()
    accno=accountdetails.account_number
    ifsc=accountdetails.IFSC
    Key=accountdetails.key
    Id=accountdetails.id
    tour_day_planners = TourDayPlanner.objects.all()
    form=UserBookingForm()

    if request.method == 'POST':

        form = UserBookingForm(request.POST)
        if form.is_valid():

            booking_instance = form.save(commit=False)
            booking_instance.package = package
            booking_instance.userid = Userprofile.objects.get(id=user_id)
            booking_instance.save()
            return render(request, 'payment.html',{'packageid':packageid1,'packageamount': packageamount, 'accno': accno, 'ifsc': ifsc, 'Key': Key, 'Id': Id,'package':package})

    else:
        form=UserBookingForm()
        return render(request, 'userbookingpackage.html',{'form': form,'packageplace': placename, 'packagename': packagename, 'packagetype': packagetype})

    return render(request, 'userbookingpackage.html', {'form': form,'packageplace': placename, 'packagename': packagename, 'packagetype': packagetype})

def user_payment(request):
    user_id = request.session.get('userid')

    accountdetails = memberaccount.objects.filter(member=user_id).first()
    key1=accountdetails.key
    amount = request.POST.get('amount')
    account_balane=accountdetails.amount

    if request.method == 'POST':
        package_id1 = request.POST.get('packageid')
        if accountdetails:
            key=request.POST.get('key')

            if key==key1:
                form = MemberAccountForm1(request.POST, instance=accountdetails)
                amount = request.POST.get('amount')

                if float(account_balane) >= float(amount):
                    if form.is_valid():

                        new_balance = float(account_balane) - float(amount)  # Convert amount to float
                        accountdetails.amount = new_balance

                        form.save()
                        package_id = request.POST.get('packageid')

                        # Use the correct parameter name when redirecting
                        return redirect('map_view', package_id=package_id)

                    else:
                        return print(form.errors)
                else:
                    return HttpResponse("Insufficient balance")
            else:
                # return render(request, 'payment.html',{'packageid': packageid1, 'packageamount': packageamount, 'accno': accno, 'ifsc': ifsc, 'Key': Key, 'Id': Id, 'package': package})

                return render(request, 'payment.html',{'packageid': package_id1,'packageamount': amount, 'accno': accountdetails.account_number, 'ifsc': accountdetails.IFSC, 'Key': accountdetails.key, 'Id': accountdetails.id})
        else:
            return HttpResponse("Account details not found")

    form = MemberAccountForm1(instance=accountdetails)
    return render(request, 'payment.html', {'form': form})

def acc_details(request):
    user_id = request.user.id

    account_details = get_object_or_404(memberaccount, member_id=user_id)

    return render(request, 'account_details.html', {'account_details': account_details})


def map_view(request, package_id):
    return render(request, 'getlocation.html', {'package_id': package_id})

def get_locations(request, package_id):
    package_detail = get_object_or_404(Package_detail, id=package_id)

    locations = Location.objects.filter(package=package_detail).all()
    locations_data = []
    for location in locations:
        location_data = {
            'place_name': location.place_name,
            'latitude': float(location.latitude),
            'longitude': float(location.longitude)
        }
        locations_data.append(location_data)
    return JsonResponse(locations_data, safe=False)