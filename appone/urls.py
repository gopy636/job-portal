from django.urls import path
from appone import views,seekerviews,providerviews

urlpatterns = [
    path("reg/",views.UserRigistation.as_view()),
    path("index/",views.ShowHome.as_view()),
    path("profile/",views.Profile.as_view(),name="profile"),
    path("addp/",views.ProfileAdd.as_view()),
    path("addjob/",views.AddJob.as_view()),
    path("jobapply/<int:id>",seekerviews.JobApply.as_view()),
    path("showseeker/<int:id>",providerviews.ShowApplicant.as_view())
]
