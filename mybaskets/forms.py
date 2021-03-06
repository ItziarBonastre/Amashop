from django.forms import ModelForm
from mybaskets.models import Category, Subcategory, Product, Basket, Customer, Review


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class SubcategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class BasketForm(ModelForm):
    class Meta:
        model = Basket
        fields = "__all__"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'surname', 'adress','city','country', 'cp','phone')
