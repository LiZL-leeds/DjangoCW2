from django.urls import path
from .views import home,flightSingle,flightBooking,logout,\
    myBooking,myProfile,dashboard,flightSearch,bookingHistory,\
    register,login,passengerAdd,bookingConfirm,flightHome,\
    flightListView,flightBook,flightDetails,errorPage

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('flightHome/', flightHome.as_view(), name='flightHome'),
    path('flightListView/', flightListView.as_view(), name='flightListView'),
    path('flightBook/', flightBook.as_view(), name='flightBook'),
    path('flightDetails/', flightDetails.as_view(), name='flightDetails'),
    path('errorPage/', errorPage.as_view(), name='errorPage'),

    path('flightSingle/',flightSingle.as_view(),name='flightSingle'),
    path('flightBooking/',flightBooking.as_view(),name='flightBooking'),
    path('flightSearch/',flightSearch.as_view(),name='flightSearch'),
    path('dashboard/', dashboard.as_view(), name='dashboard'),
    path('myProfile/', myProfile.as_view(), name='myProfile'),
    path('myBooking/', myBooking.as_view(), name='myBooking'),
    path('bookingHistory/', bookingHistory.as_view(), name='bookingHistory'),
    path('logout/', logout.as_view(), name='logout'),
    path('login/', login.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('passengerAdd/', passengerAdd.as_view(), name='passengerAdd'),
    path('logout/bookingConfirm/', bookingConfirm.as_view(), name='bookingConfirm'),
    path('login/bookingConfirm/', bookingConfirm.as_view(), name='bookingConfirm'),
]