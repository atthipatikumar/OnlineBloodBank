"""OnlineBloodBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Application import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
        url(r'^$',views.Index ),
        url(r'^signup/',views.signup ),
        url(r'^login_view/',views.login_view ),
        url(r'^create-blood-group/',views.CreateBloodGroup  ,name="CreateBloodGroup"),
        url(r'^donarlist/',views.donarlist ),
        url(r'^dashbord/',views.dashbord ),
        url(r'^list/',views.list ),
        url(r'^update/([0-9]+)/',views.updateprofile ),
        url(r'^logout/',views.signout ),
        url(r'^post/',views.post_view ),
        url(r'^post_list/',views.post_list ),
]
