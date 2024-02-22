# from .models import Category


# def menu_links(request):
#     links = Category.objects.all()
#     return dict(links=links)

from .models import ParentCategory

def categories(request):
    categories = ParentCategory.objects.all()
    return {'categories': categories}
