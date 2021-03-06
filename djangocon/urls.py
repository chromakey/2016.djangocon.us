from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from symposion import views as symposion_views
from djangocon import views as djangocon_views


urlpatterns = [
    url(r'^$', djangocon_views.homepage, name='home'),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact_form.urls')),
]

# Symposion urls
urlpatterns += [
    url(r'^dashboard/', symposion_views.dashboard, name='dashboard'),
    url(r'^proposals/', include('symposion.proposals.urls')),
    url(r'^reviews/', include('symposion.reviews.urls')),
    url(r'^schedule/', include('symposion.schedule.urls')),
    url(r'^speaker/', include('symposion.speakers.urls')),
    url(r'^sponsors/', include('symposion.sponsorship.urls')),
    url(r'^teams/', include('symposion.teams.urls')),
]

# Pinax urls
urlpatterns += [
    url(r'^boxes/', include('pinax.boxes.urls')),
    url(r'^blog/', include('pinax.blog.urls')),
    url(r'^', include('pinax.pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
