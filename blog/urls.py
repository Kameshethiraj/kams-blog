from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name ="starting-page"),
    path("posts", views.AllPostView.as_view(), name = "posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name = "post_view"), #/posts/my-first-project
    path("read-later", views.ReadLaterView.as_view(), name = "read-later"),
]

# here slug automatically takes the parameter we added in post href url