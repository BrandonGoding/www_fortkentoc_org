from website.models import EventCategoryTextChoices, EventTagTextChoices

EVENTS = [
    {
        "title": "Seasonal Ski Rentals",
        "program_dates": [
            {"date": "2023-11-18", "start_time": "13:00", "end_time": "15:00"},
            {"date": "2023-12-03", "start_time": "13:00", "end_time": "15:00"},
        ],
    },
    {
        "title": "Welcome Winter Celebration",
        "program_dates": [
            {"date": "2023-12-02", "start_time": "17:00", "end_time": "20:00"}
        ],
    },
    {
        "title": "High School Skate Race",
        "program_dates": [{"date": "2023-12-12"}],
    },
    {
        "title": "Ben Paradis Invitational",
        "program_dates": [{"date": "2023-12-28", "cancelled": True}],
    },
    {
        "title": "Jalbert Youth SKi Program",
        "program_dates": [
            {"date": "2023-12-30", "start_time": "13:00", "end_time": "14:00"},
            {"date": "2024-01-13", "start_time": "13:00", "end_time": "14:00"},
            {"date": "2024-01-27", "start_time": "13:00", "end_time": "14:00"},
            {"date": "2024-02-10", "start_time": "13:00", "end_time": "14:00"},
            {"date": "2024-02-24", "start_time": "13:00", "end_time": "14:00"},
            {"date": "2024-03-09", "start_time": "13:00", "end_time": "14:00"},
        ],
    },
    {
        "title": "2024 Snowshoe Series",
        "program_dates": [
            {"date": "2023-12-31", "start_time": "13:00", "end_time": "14:30"},
            {"date": "2024-01-07", "start_time": "13:00", "end_time": "14:30"},
            {"date": "2024-01-20", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-02-03", "start_time": "13:00", "end_time": "14:30"},
            {"date": "2024-02-18", "start_time": "13:00", "end_time": "14:30"},
            {"date": "2024-03-03", "start_time": "13:00", "end_time": "14:30"},
            {"date": "2024-03-16", "start_time": "18:30", "end_time": "20:00"},
        ],
    },
    {
        "title": "Ladies Ski Night",
        "program_dates": [
            {"date": "2024-01-04", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-01-11", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-01-18", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-01-25", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-02-01", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-02-08", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-02-15", "start_time": "18:30", "end_time": "20:00"},
        ],
    },
    {
        "title": "Open Ski Night",
        "program_dates": [
            {"date": "2024-01-09", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-01-16", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-01-23", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-01-30", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-02-06", "start_time": "18:30", "end_time": "20:00"},
            {"date": "2024-02-13", "start_time": "18:30", "end_time": "20:00"},
        ],
    },
    {
        "title": "Eastern Biathlon Regional Cup",
        "program_dates": [
            {"date": "2024-01-19", "start_time": "12:00"},
            {"date": "2024-01-20", "start_time": "08:00"},
            {"date": "2024-01-21", "start_time": "08:00"},
        ],
    },
    {
        "title": "High School Classic Race",
        "program_dates": [{"date": "2024-01-23", "start_time": "15:00"}],
    },
    {
        "title": "Middle School Classic Race",
        "program_dates": [{"date": "2024-01-24", "start_time": "15:30"}],
    },
    {
        "title": "UMFK Indoor Biathlon",
        "program_dates": [
            {"date": "2024-02-17", "start_time": "12:00", "end_time": "16:00"}
        ],
    },
    {
        "title": "Frosty Bites",
        "program_dates": [{"date": "2024-03-10", "cancelled": True}],
    },
    {
        "title": "USBA Nationals",
        "program_dates": [
            {"date": "2024-03-21", "start_time": "09:00"},
            {"date": "2024-03-22", "start_time": "09:00"},
            {"date": "2024-03-23", "start_time": "09:00"},
            {"date": "2024-03-24", "start_time": "09:00"},
        ],
        "category": EventCategoryTextChoices.US_BIATHLON_ASSOCIATION,
        "tags": [EventTagTextChoices.CHAMPIONSHIP_EVENT],
        "show_in_past_events": True,
        "url": "/events/usba-nationals/",
    },
    {
        "title": "U15 Biathlon Camp",
        "program_dates": [
            {"date": "2024-07-22"},
            {"date": "2024-07-23"},
            {"date": "2024-07-24"},
            {"date": "2024-07-25"},
        ],
        "category": EventCategoryTextChoices.TRAINING_CAMP,
        "tags": [EventTagTextChoices.BIATHLON],
        "banner_image_url": "/website/img/biathlon_camp/campbanner.jpg",
        "url": "/events/2024-biathlon-camp/",
    },
    {
        "title": "U18 Biathlon Camp",
        "program_dates": [
            {"date": "2024-07-27"},
            {"date": "2024-07-28"},
            {"date": "2024-07-29"},
            {"date": "2024-07-30"},
            {"date": "2024-07-31"},
        ],
        "category": EventCategoryTextChoices.TRAINING_CAMP,
        "tags": [EventTagTextChoices.BIATHLON],
        "banner_image_url": "/website/img/biathlon_camp/campbanner.jpg",
        "url": "/events/2024-biathlon-camp/",
    },
    {
        "title": "2024 Summer Nordic Camp",
        "program_dates": [
            {"date": "2024-06-28"},
            {"date": "2024-06-29"},
            {"date": "2024-06-30"},
            {"date": "2024-07-01"},
        ],
        "category": EventCategoryTextChoices.TRAINING_CAMP,
        "tags": [EventTagTextChoices.NORDIC],
        "banner_image_url": "/website/img/biathlon_camp/campbanner.jpg",
        "url": "/events/2024-nordic-camp/",
    },
    {
        "title": "2024 Diamond Trail Hikes",
        "program_dates": [
            {"date": "2024-07-11"},
            {"date": "2024-07-25"},
            {"date": "2024-08-08"},
            {"date": "2024-08-22"},
            {"date": "2024-09-05"},
            {"date": "2024-09-19"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.SOCIAL_EVENT],
        "url": "https://www.fortkentoc.org/website/2024diamonhikes.jpeg",
    },
    {
        "title": "BBQ & Band Fundraiser",
        "program_dates": [
            {"date": "2024-08-17"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.SOCIAL_EVENT],
        "url": "https://www.fortkentoc.org/website/2024diamonhikes.jpeg",
    },
    {
        "title": "Disc Golf Tournament",
        "program_dates": [
            {"date": "2024-08-17"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.SOCIAL_EVENT],
        "url": "https://www.fortkentoc.org/website/2024diamonhikes.jpeg",
    },
    {
        "title": "Raffle & Silent Auction",
        "program_dates": [
            {"date": "2024-08-17"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.SOCIAL_EVENT],
        "url": "https://www.fortkentoc.org/website/2024diamonhikes.jpeg",
    },
    {
        "title": "Seasonal Ski Rental",
        "program_dates": [
            {"date": "2024-11-16", "start_time": "13:00", "end_time": "15:00"},
            {"date": "2024-12-08", "start_time": "13:00", "end_time": "15:00"},
        ],
    },
    {
        "title": "Ford Sayre Ski Camp",
        "program_dates": [
            {"date": "2024-11-23"},
            {"date": "2024-11-24"},
            {"date": "2024-11-25"},
            {"date": "2024-11-26"},
            {"date": "2024-11-27"},
            {"date": "2024-11-28"},
            {"date": "2024-11-29"},
            {"date": "2024-11-30"},
        ],
        "category": EventCategoryTextChoices.TRAINING_CAMP,
        "tags": [EventTagTextChoices.NORDIC],
    },
    {
        "title": "Welcome Winter",
        "program_dates": [
            {"date": "2024-12-07", "start_time": "17:00", "end_time": "20:00"},
        ],
    },
    {
        "title": "High School Nordic Race",
        "program_dates": [
            {"date": "2024-12-10", "start_time": "15:00", "end_time": "17:00"},
        ],
    },
    {
        "title": "UMFK Laser Biathlon",
        "program_dates": [
            {"date": "2024-12-13"},
            {"date": "2024-12-14"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.HOSTED_BY_UMFK],
    },
    {
        "title": "Christmas Ski Camp",
        "program_dates": [
            {"date": "2024-12-26"},
            {"date": "2024-12-27"},
            {"date": "2024-12-28"},
            {"date": "2024-12-29"},
            {"date": "2024-12-30"},
        ],
        "category": EventCategoryTextChoices.TRAINING_CAMP,
        "tags": [EventTagTextChoices.NORDIC],
    },
    {
        "title": "Ben Paradis Invitational Race",
        "program_dates": [
            {"date": "2024-12-27", "start_time": "13:00", "end_time": "15:00"},
        ],
    },
    {
        "title": "IBU Regional Biathlon Cup",
        "program_dates": [
            {"date": "2025-01-31"},
            {"date": "2025-02-01"},
            {"date": "2025-02-02"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.NORDIC],
    },
    {
        "title": "Frosty Bites",
        "program_dates": [
            {"date": "2025-02-09", "start_time": "13:00", "end_time": "15:30"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.NORDIC],
    },
    {
        "title": "Pat’s Ride",
        "program_dates": [
            {"date": "2025-02-27"},
        ],
        "category": EventCategoryTextChoices.COMMUNITY_EVENT,
        "tags": [EventTagTextChoices.SOCIAL_EVENT],
    },
]
