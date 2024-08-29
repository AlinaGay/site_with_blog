from django.urls import path

urlspattern = [
  path(""),
  path("posts"),
  path("posts/<slug:slug>")
]