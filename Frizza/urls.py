from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Frizza.views.home', name='home'),
    # url(r'^Frizza/', include('Frizza.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^$', views.LoginView.as_view(), name='login')#,
    #url(r'^disclaimer/', include('disclaimer.urls')),
    #url(r'^admin/', include('admin.urls')),
    #url(r'^toppings/', include('toppings.urls')),
    #url(r'^allergies/', include('allergies.urls')),
    #url(r'^pizza/', include('pizza.urls')),
    #url(r'^crust/', include('crust.urls')),
    #url(r'^sauce/', include('sauce.urls')),
    #url(r'^confirmation/', include('confirmation.urls')),
    #url(r'^goodbye/', include('goodbye.url')),
    #url(r'^return/', incude('return.url'))
)
