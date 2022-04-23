from django.views.generic.base import TemplateView
from gen.mixins import MainPageMixin
from gen.mixins import get_settings_template
from home.models import SliderHome
from gen.catalog.helpers import ProductHelper
from gen.catalog.forms.product_comment import CommentForm
from catalog.models import Product


class BaseHomePageView(MainPageMixin, TemplateView):
    template_name = 'home/templates/home.html'

    def get_context_data(self, **kwargs):
        context = super(BaseHomePageView, self).get_context_data(**kwargs)

        context['slider_home'] = SliderHome.objects.all()
        context['new_products'] = ProductHelper.get_new()
        context['bestseller_products'] = ProductHelper.get_bestseller()
        context['home'] = get_settings_template() and get_settings_template().home

        if Product.objects.first():
            initial = {'obj': Product.objects.first(), 'request': self.request}
            context['comment_form'] = CommentForm(initial=initial)

        if context['home'] and context['home'].blog:
            posts = context['home'].blog.post_set
            context['posts'] = posts.exists() and posts.filter(is_show=True)

        return context
