from django.db import models


COLOR_CODES = {
    "gray": {
        "100": "#f3f4f6",
        "200": "#e5e7eb",
        "800": "#1f2937",
        "900": "#111827",
    },
    "red": {
        "100": "#fde8e8",
        "200": "#fbd5d5",
        "800": "#9b1c1c",
        "900": "#771d1d",
    },
    "yellow": {
        "100": "#fdf6b2",
        "200": "#fce96a",
        "800": "#723b13",
        "900": "#633112",
    },
    "green": {
        "100": "#def7ec",
        "200": "#bcf0da",
        "800": "#03543f",
        "900": "#014737",
    },
    "blue": {
        "100": "#e1effe",
        "200": "#c3ddfd",
        "800": "#1e429f",
        "900": "#233876",
    },
    "purple": {
        "100": "#e5edff",
        "200": "#cddbfe",
        "800": "#42389d",
        "900": "#362f78",
    },
    "pink": {
        "100": "#fce8f3",
        "200": "#fad1e8",
        "800": "#99154b",
        "900": "#751a3d",
    },
}


class ColorChoices(models.TextChoices):
    GRAY = "gray", "Gray"
    RED = "red", "Red"
    YELLOW = "yellow", "Yellow"
    GREEN = "green", "Green"
    BLUE = "blue", "Blue"
    PURPLE = "purple", "Purple"
    PINK = "pink", "Pink"

    @staticmethod
    def get_category_color(category):
        if category == category.AROOSTOOK_ATHLETICS:
            return ColorChoices.RED
        if category == category.MEMBERSHIP_EVENT:
            return ColorChoices.YELLOW
        if category == category.COMMUNITY_EVENT:
            return ColorChoices.GREEN
        if category == category.US_BIATHLON_ASSOCIATION:
            return ColorChoices.BLUE
        if category == category.JALBERT_PROGRAM:
            return ColorChoices.PURPLE
        if category == category.TRAINING_CAMP:
            return ColorChoices.PINK

    @property
    def color_code(self):
        color = self.value
        return COLOR_CODES[color]


class EventCategoryTextChoices(models.TextChoices):
    AROOSTOOK_ATHLETICS = "aroostook_athletics", "Aroostook Athletics"
    MEMBERSHIP_EVENT = "membership_event", "Membership Event"
    COMMUNITY_EVENT = "community_event", "Community Event"
    US_BIATHLON_ASSOCIATION = (
        "us_biathlon_association",
        "US Biathlon Association",
    )
    JALBERT_PROGRAM = "jalbert_program", "Jalbert Program"
    TRAINING_CAMP = "training_camp", "Training Camp"


class EventTagTextChoices(models.TextChoices):
    HIGH_SCHOOL_RACE = "high_school_race", "High School Race"
    MIDDLE_SCHOOL_RACE = "middle_school_race", "Middle School Race"
    INVITATIONAL = "invitational", "Invitational"
    BOARD_ELECTIONS = "board_elections", "Board Elections"
    SOCIAL_EVENT = "social_event", "Social Event"
    RENTAL_SHOP = "rental_shop", "Rental Shop"
    MEMBERSHIP_DRIVE = "membership_drive", "Membership Drive"
    HOSTED_BY_UMFK = "hosted_by_umfk", "Hosted By UMFK"
    CHAMPIONSHIP_EVENT = "championship_event", "Championship Event"
    FUNDRAISER = "fundraiser", "Fundraiser"
    SKI_LESSONS = "ski_lessons", "Ski Lessons"
    LADIES_ONLY = "ladies_only", "Ladies Only"
    POKER_RUN = "poker_run", "Poker Run"
    BIATHLON = "biathlon", "Biathlon"
    NORDIC = "nordic", "Nordic"

    @property
    def tag_color(tag):
        if tag == EventTagTextChoices.HIGH_SCHOOL_RACE:
            return ColorChoices.GRAY
        if tag == EventTagTextChoices.MIDDLE_SCHOOL_RACE:
            return ColorChoices.RED
        if tag == EventTagTextChoices.INVITATIONAL:
            return ColorChoices.YELLOW
        if tag == EventTagTextChoices.BOARD_ELECTIONS:
            return ColorChoices.GREEN
        if tag == EventTagTextChoices.SOCIAL_EVENT:
            return ColorChoices.BLUE
        if tag == EventTagTextChoices.RENTAL_SHOP:
            return ColorChoices.PURPLE
        if tag == EventTagTextChoices.MEMBERSHIP_DRIVE:
            return ColorChoices.GRAY
        if tag == EventTagTextChoices.HOSTED_BY_UMFK:
            return ColorChoices.RED
        if tag == EventTagTextChoices.CHAMPIONSHIP_EVENT:
            return ColorChoices.YELLOW
        if tag == EventTagTextChoices.SKI_LESSONS:
            return ColorChoices.GREEN
        if tag == EventTagTextChoices.LADIES_ONLY:
            return ColorChoices.BLUE
        if tag == EventTagTextChoices.POKER_RUN:
            return ColorChoices.PURPLE
        if tag == EventTagTextChoices.BIATHLON:
            return ColorChoices.RED
        if tag == EventTagTextChoices.NORDIC:
            return ColorChoices.PURPLE


class Event(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=EventCategoryTextChoices.choices)


class ProgramDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
