from django.conf.urls import patterns, url, include
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Basket
from forms import BasketForm
from views import BasketDetail, BasketCreate, BasketDelete, SubcategoryDetail, CategoryDetail, ProductDetail, \
    BasketList, SubcategoryList, CategoryList, ProductList, \
    mainpage, UserProfileCreate, UserProfileDetail, UserProfile, UserProfileForm

urlpatterns = patterns('',


    url(r'^$', mainpage, name='home'),
    # List all user baskets: /mybaskets/
    url(r'^baskets/$', BasketList.as_view(), name='basket'),
    # BAsket details, ex.: /mybaskets/baskets/1
    url(r'^baskets/(?P<pk>\d+)/$', BasketDetail.as_view(), name='basket_detail'),
    # Create a basket: /mybaskets/baskets/create/
    url(r'^baskets/create/$', BasketCreate.as_view(), name='basket_create'),
    # Edit basket details, ex: /mybaskets/baskets/edit/1
    url(r'^baskets/edit/(?P<pk>\d+)/$', UpdateView.as_view(
        model=Basket,
        form_class=BasketForm,
        template_name='mybaskets/form.html'),
        name='basket_edit'),
    # Delete basket, ex: /mybaskets/baskets/delete/1
    url(r'^baskets/delete/(?P<pk>\d+)/$', BasketDelete.as_view(), name='delete_basket'),
    # List all subcategories: mybaskets/subcategory/
    url(r'^subcategories/$', SubcategoryList.as_view(), name='subcategories'),
    # Subcategories details, ex: /mybaskets/subcategories/1
    url(r'^subcategories/(?P<pk>\d+)/$', SubcategoryDetail.as_view(), name='subcategory_detail'),
    # List all Categories: mybaskets/categories/
    url(r'^categories/$', CategoryList.as_view(), name='categories'),
    # Category details, ex: /mybaskets/categories/1
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category_detail'),
    # List all Products: mybaskets/products/
    url(r'^products/$', ProductList.as_view(), name='products'),
    # Product details, ex: /mybaskets/products/1
    url(r'^products/(?P<pk>\d+)/$', SongDetail.as_view(), name='song_detail'),
    # User profile details, ex: /mybaskets/user/1/userprofile/
    url(r'^user/(?P<pk>\d+)/userprofile/$', UserProfileDetail.as_view(), name='userprofile_detail'),
    # Create a User profile: /mybaskets/user/1/userprofile/create/
    url(r'^user/(?P<pk>\d+)/userprofile/create/$', UserProfileCreate.as_view(), name='userprofile_create'),
    # Edit User profile details, ex: /mybaskets/user/1/userprofile/edit/1
    url(r'^user/(?P<pk>\d+)/userprofile/edit/(?P<id>\d+)/$', UpdateView.as_view(
        model=UserProfile,
        form_class=UserProfileForm,
        template_name='mybaskets/form.html'),
        name='userprofile_edit'),
    url(r'^subcategory/(?P<pk>\d+)/reviews/create/$', 'mybaskets.views.review', name='review_create'),

    )

