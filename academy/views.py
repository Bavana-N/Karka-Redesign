from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import Course


def home(request):
    courses = Course.objects.all()[:3]
    return render(request, "index.html", {"courses": courses})


def course_list(request):
    courses = Course.objects.all()

    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "").strip()

    if search:
        courses = courses.filter(name__icontains=search)

    if category:
        courses = courses.filter(category=category)

    categories = Course.objects.values_list(
        "category",
        flat=True
    ).distinct()

    return render(
        request,
        "courses.html",
        {
            "courses": courses,
            "categories": categories,
            "selected_category": category,
            "search_query": search,
        }
    )


def course_detail(request, pk):

    course = get_object_or_404(Course, pk=pk)

    return render(
        request,
        "course-detail.html",
        {
            "course": course
        }
    )


# =====================================================
# SIGN UP
# =====================================================

def signup_view(request):

    if request.user.is_authenticated:
        next_url = request.GET.get("next")

        if next_url:
            return redirect(next_url)

        return redirect("home")

    next_url = request.GET.get("next", "")

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            return render(
                request,
                "signup.html",
                {
                    "error": "Passwords do not match.",
                    "next": next_url,
                }
            )

        if User.objects.filter(username=username).exists():

            return render(
                request,
                "signup.html",
                {
                    "error": "Username already exists.",
                    "next": next_url,
                }
            )

        if User.objects.filter(email=email).exists():

            return render(
                request,
                "signup.html",
                {
                    "error": "Email already exists.",
                    "next": next_url,
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # After registration → Login
        login_url = "/login/"

        if next_url:
            login_url += "?next=" + next_url

        return redirect(login_url)

    return render(
        request,
        "signup.html",
        {
            "next": next_url
        }
    )


# =====================================================
# LOGIN
# =====================================================

def login_view(request):

    if request.user.is_authenticated:

        next_url = request.GET.get("next")

        if next_url:
            return redirect(next_url)

        return redirect("home")

    next_url = request.GET.get("next", "")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if next_url:
                return redirect(next_url)

            return redirect("home")

        return render(
            request,
            "login.html",
            {
                "error": "Invalid username or password.",
                "next": next_url,
            }
        )

    return render(
        request,
        "login.html",
        {
            "next": next_url
        }
    )


# =====================================================
# LOGOUT
# =====================================================

def logout_view(request):

    logout(request)

    return redirect("home")


# =====================================================
# ENROLL
# =====================================================

def enroll_course(request, pk):

    course = get_object_or_404(Course, pk=pk)

    # User is NOT logged in
    if not request.user.is_authenticated:

        signup_url = f"/signup/?next=/course/{pk}/enroll/"

        return redirect(signup_url)

    # User is logged in and confirms enrollment
    if request.method == "POST":

        return render(
            request,
            "enroll-success.html",
            {
                "course": course
            }
        )

    # Logged-in user → show enrollment page
    return render(
        request,
        "enroll.html",
        {
            "course": course
        }
    )


def why_karka(request):

    return render(
        request,
        "why-karka.html"
    )
def contact(request):
    return render(request, "contact.html")