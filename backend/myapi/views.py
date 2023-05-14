
from django.forms import SlugField
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product,Category, Review
from .forms import ReviewForm

class ProductListView(ListView):
    paginate_by = 9
    context_object_name = 'products_list'

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug']
        )
        return Product.objects.filter(
            category__slug=self.category.slug
        ).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProductDetail(DetailView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['form'] = ReviewForm
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        self.object = super(ProductDetail, self).get_object()
        context = super(ProductDetail, self).get_context_data()
        context['form'] = ReviewForm
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = self.object
            new_review.save()

        else:
            context['form'] = form

        return self.render_to_response(context=context)
