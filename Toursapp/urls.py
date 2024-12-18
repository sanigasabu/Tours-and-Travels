from.views import *
from django.urls import path

urlpatterns = [
    path('register/', user_registraction.as_view(), name='Registraction'),
    path('',login_view,name='login'),
    path('home/', home, name='index'),
    path('adminpanel/', adminpanel, name='admin_panel'),
    path('add_flight/', add_flight, name='add_flight'),
    path('manage_flights/', manage_flights, name='manage_flights'),
    path('edit_flight/<int:id>/', edit_flight, name='edit_flights'),
    path('delete_flight/<int:id>/', delete_flight, name='delete_flights'),
    path('add_packageplaces/', add_packageplace, name='add_packageplace'),
    path('manage_packageplaces/', manage_packageplaces, name='manage_packageplace'),
    path('edit_packageplaces/<int:id>/', edit_packageplaces, name='edit_packageplace'),
    path('delete_packageplaces/<int:id>/', delete_packageplaces, name='delete_packageplace'),
    path('add_packagedetails/', add_packagedetails, name='add_packagedetails'),
    path('manage_Packagedetails/', manage_Packagedetails, name='manage_packagedetails'),
    path('edit_Packagedetails/<int:id>/', edit_Packagedetails, name='edit_Packagedetails'),
    path('delete_Packagedetails/<int:id>/', delete_Packagedetails, name='delete_Packagedetails'),
    path('add_planer/', add_planner, name='add_planner'),
    path('manage_planer/', manage_planner, name='manage_planner'),
    path('edit_planer/<int:id>/', edit_planner, name='edit_planers'),
    path('delete_planer/<int:id>/', delete_planner, name='delete_planers'),
    path('add_hotel/', add_hotel, name='add_hotel'),
    path('manage_hotel/', manage_hotel, name='manage_hotels'),
    path('edit_hotel/<int:id>/', edit_hotel, name='edit_hotels'),
    path('delete_hotel/<int:id>/', delete_hotel, name='delete_hotels'),
    path('view_booking/', view_user_bookings, name='view_booking'),
    path('view_user/', view_user, name='view_user'),
    path('user_packageplaceview/', user_packageplaceview, name='user_packageplace'),
    path('user_packageview/<int:pk>', user_packageview, name='user_viewpackages'),
    path('user_plannerview/<int:pk>/<int:packageplaceid>/', user_plannerview, name='user_viewdayplanner'),
    path('userbooking/<int:packageid>/<int:packageplaceid>/', package_booking, name='userbooking'),
    path('payment/', user_payment, name='payment'),
    path('history/', history, name='history'),
    path('save_location/', save_location, name='save_location'),
    path('account-details/', user_registraction.as_view(), name='account_details'),
    path('user_account/', acc_details, name='user_account'),
    path('get_locations/<int:package_id>/', get_locations, name='get_locations'),
    path('map_view/<int:package_id>/', map_view, name='map_view'),

]