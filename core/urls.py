from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.contact.urls")),
    path("", include("apps.website.urls")),
    path("", include("apps.accounts.urls")),
    path("", include("apps.shop.urls")),
    path("", include("apps.cart.urls")),
    path("", include("apps.dashboard.urls")),
    path("", include("apps.order.urls")),
    path("", include("apps.payment.urls")),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.SHOW_DEBUGGER_TOOLBAR:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')), ]
