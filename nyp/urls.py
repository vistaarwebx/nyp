
from django.contrib import admin
from django.urls import path
from youth.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name= 'home'),
    path('admin_index',ADINDEX,name= 'admin_index'),
    path('aboutdrsn',ABOUTDR,name= 'aboutdrsn'),
    path('whoweare',WHOWEARE,name= 'whoweare'),
    path('ourteam',OURTEAM,name= 'ourteam'),
    path('visionmission',VISIONMISSION,name= 'visionmission'),
    path('registration/',Unitregistration,name= 'unitregistration'),
    path('Logout/',LOGOUT,name='Logout'),
    path('Login/',LOGIN,name='Login'),
    path('email/',Email,name = 'email'),
    path('video/',Video,name = 'video'),
    path('job_internship/',JOB_INTERNSHIP,name = 'job_internship'),
    path('volunteer/',VOLUNTEER,name = 'volunteer'),
    path('media/',Media,name = 'media'),
    path('post/<int:po_id>/',POST,name = 'post'),
    path('press_single/<int:pr_id>/',PRESS_single,name = 'press_single'),
    path('sinbook/<int:bu_id>/',SingleBook,name = 'sinbook'),
    path('book/',BOOK,name = 'book'),
    path('camps/',CAMPS,name = 'camps'),
    path('press/',PRESS,name = 'press'),
    path('contact/',CONTACT,name = 'contact'),
    path('gallery/',GALLERY,name = 'gallery'),
    path('terms_cond/',TERMS_COND,name = 'terms_cond'),
    path('book_delete/<int:fb_id>/', BOOK_delete, name='book_delete'),
    path('camp_delete/<int:ca_id>/', CAMP_delete, name='camp_delete'),
    path('press_delete/<int:pr_id>/', PRESS_delete, name='press_delete'),
    path('media_delete/<int:me_id>/', MEDIA_delete, name='media_delete'),
    path('gallery_delete/<int:ga_id>/', GALLERY_delete, name='gallery_delete'),
    path('volunteer_delete/<int:vo_id>/', VOLUNTEER_delete, name='volunteer_delete'),
    path('job_delete/<int:jd_id>/',JOB_delete, name='job_delete'),
    path('nyp_delete/<int:ny_id>/',NYP_delete, name='nyp_delete'),
    path('volunteer_activate/<int:pk>/',VOLUNTEER_ACTIVATE, name='volunteer_activate'),
    path('job_activate/<int:pk>/',JOB_ACTIVATE, name='job_activate'),
    path('nyp_activate/<int:pk>/',NYP_ACTIVATE, name='nyp_activate'),
    path('unit_request/',UNIT_REQUEST,name = 'unit_request'),
    path('active_units/',ACTIVE_UNITS,name = 'active_units'),
    path('expired___volunteers/',VOLUNTEER_REQUEST,name = 'expired___volunteers'),
    path('active__volunteers/',ACTIVE_VOLUNTEER,name = 'active__volunteers'),
    path('expired_jobs/',JOB_REQUEST,name = 'expired_jobs'),
    path('active_jobs/',ACTIVE_JOB,name = 'active_jobs'),
    path('nypsingle/<int:nys_id>/',NYP_SINGLE, name='nypsingle'),
    path('volunteersingle/<int:vos_id>/',VOLUNTEER_SINGLE, name='volunteersingle'),
    path('jobsingle/<int:jos_id>/',JOB_SINGLE, name='jobsingle'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
