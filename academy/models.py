from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    duration = models.CharField(max_length=50)

    short_description = models.TextField()

    overview = models.TextField()

    what_you_learn = models.TextField(
        help_text="Enter each learning point on a new line."
    )

    projects = models.TextField(
        help_text="Enter each project on a new line."
    )

    career_opportunities = models.TextField(
        help_text="Enter each career role on a new line."
    )

    image = models.ImageField(
        upload_to="courses/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Convert learning points into a list
    @property
    def learning_points(self):
        return [
            item.strip()
            for item in self.what_you_learn.splitlines()
            if item.strip()
        ]

    # Convert projects into a list
    @property
    def project_list(self):
        return [
            item.strip()
            for item in self.projects.splitlines()
            if item.strip()
        ]

    # Convert career opportunities into a list
    @property
    def career_list(self):
        return [
            item.strip()
            for item in self.career_opportunities.splitlines()
            if item.strip()
        ]

class Event(models.Model):

    EVENT_TYPES = [
        ("Event", "Event"),
        ("Hackathon", "Hackathon"),
        ("Workshop", "Workshop"),
        ("Webinar", "Webinar"),
    ]

    title = models.CharField(max_length=200)

    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPES,
        default="Event"
    )

    description = models.TextField()

    event_date = models.DateTimeField()

    location = models.CharField(
        max_length=200,
        blank=True
    )

    registration_url = models.URLField(
        blank=True
    )

    banner = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
