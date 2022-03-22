from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "kamil",
        "date": date(2022, 6, 12),
        "title": "Mountain Hiking",
        "exerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi consequatur similique.",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi consequatur similique, corporis totam repudiandae culpa quod tenetur laborum voluptatem autem dicta cum, quaerat aut sequi dolore cupiditate fugiat natus! Tempora!

                    Eligendi consequatur similique, corporis totam repudiandae culpa quod tenetur laborum voluptatem autem dicta cum, quaerat aut sequi dolore cupiditate fugiat natus! Tempora!
                """
    },
    {
        "slug": "Bike-in-the-bare-mountains",
        "image": "mountains.jpg",
        "author": "kamil",
        "date": date(2020, 3, 1),
        "title": "Mountain Biking",
        "exerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi consequatur similique.",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi consequatur similique, corporis totam repudiandae culpa quod tenetur laborum voluptatem autem dicta cum, quaerat aut sequi dolore cupiditate fugiat natus! Tempora!

                    Eligendi consequatur similique, corporis totam repudiandae culpa quod tenetur laborum voluptatem autem dicta cum, quaerat aut sequi dolore cupiditate fugiat natus! Tempora!
                """
    },
    {
        "slug": "Programming-in-the-mountains",
        "image": "mountains.jpg",
        "author": "kamil",
        "date": date(2021, 10, 11),
        "title": "Mountain Programing",
        "exerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi consequatur similique.",
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi consequatur similique, corporis totam repudiandae culpa quod tenetur laborum voluptatem autem dicta cum, quaerat aut sequi dolore cupiditate fugiat natus! Tempora!

                    Eligendi consequatur similique, corporis totam repudiandae culpa quod tenetur laborum voluptatem autem dicta cum, quaerat aut sequi dolore cupiditate fugiat natus! Tempora!
                """
    }

]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })