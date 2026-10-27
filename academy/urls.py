from django.urls import path

from . import views


urlpatterns = [

    # Home
    path(
        "",
        views.home,
        name="home"
    ),
    
    # Events and Hackathons
    path(
        "events/",
        views.events_page,
        name="events"
    ),

    # Courses
    path(
        "courses/",
        views.course_list,
        name="course_list"
    ),

    # Course Details
    path(
        "course/<int:pk>/",
        views.course_detail,
        name="course_detail"
    ),

    # Why Karka
    path(
        "why-karka/",
        views.why_karka,
        name="why_karka"
    ),

    # Authentication
    path(
        "signup/",
        views.signup_view,
        name="signup"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    # Enrollment
    path(
        "course/<int:pk>/enroll/",
        views.enroll_course,
        name="enroll_course"
    ),
    path("contact/", views.contact, name="contact"),
]