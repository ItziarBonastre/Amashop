from django.shortcuts import render
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import DetailView, DeleteView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout

from models import Category, Subcategory, Product, Basket, UserProfile, ReleaseReview
from forms import BasketForm, UserProfileForm


class BasketList(ListView):
    model = Basket
    queryset = Basket.objects.all()
    context_object_name = 'latest_basket_list'
    template_name = 'mybaskets/basket_list.html'


class BasketDetail(DetailView):
    model = Basket
    template_name = 'mybaskets/basket_detail.html'


class ReleaseList(ListView):
    model = Subcategory
    queryset = Subcategory.objects.all()
    context_object_name = 'all_subcategories_list'
    template_name = 'mybaskets/subcategory_list.html'


class ReleaseDetail(DetailView):
    model = Subcategory
    template_name = 'mybaskets/subcategory_detail.html'


class CategoryList(ListView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'all_categories_list'
    template_name = 'mybaskets/category_list.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'mybaskets/category_detail.html'


class ProductList(ListView):
    model = Product
    queryset = Product.objects.all()
    context_object_name = 'all_products_list'
    template_name = 'mybaskets/product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'mybaskets/product_detail.html'


class BasketCreate(CreateView):
    model = Basket
    template_name = 'mybaskets/form.html'
    form_class = BasketForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BasketCreate, self).form_valid(form)


class BasketDelete(DeleteView):
    model = Basket
    success_url = '/mybaskets/baskets'


class UserProfileCreate(CreateView):
    model = UserProfile
    template_name = 'mybaskets/form.html'
    form_class = UserProfileForm

    def form_valid(self, form):
        form.instance.id = self.request.user.id
        form.instance.user = self.request.user
        return super(UserProfileCreate, self).form_valid(form)


class UserProfileDetail(DetailView):
    model = UserProfile
    template_name = 'mybaskets/userprofile_detail.html'


def mainpage(request):
    return render_to_response(
        'mybaskets/mainpage.html',
        {
            'user': request.user,
            'userprofile': UserProfile.objects.filter(user__id=request.user.id)
        }
    )


def log_out(request):
    logout(request)
    return render_to_response(
        'registration/logout.html'
    )





def review(request, pk):
    release = get_object_or_404(Release, pk=pk)
    new_review = ReleaseReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        subcategory=subcategory)
    new_review.save()
    return HttpResponseRedirect(urlresolvers.reverse('mybaskets:subcategory_detail', args=(Subcategory.id,)))
