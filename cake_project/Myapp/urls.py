from django.urls import path
from Myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("product", views.product, name="product"),
    path("testimonial", views.testimonial, name="testimonial"),
    path("service", views.service, name="service"),
    path("order", views.order, name="order"),
    path("order1", views.order1, name="order1"),
    path("order2", views.order2, name="order2"),
    path("signin", views.signin, name="signin"),
    path("addData",views.addData,name="addData"),
    path("addData1",views.addData1,name="addData1"),
    path("addData2",views.addData2,name="addData2"),
    path("details", views.details, name="details"),
    path("logout_user", views.logout_user, name="logout_user"),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
]
