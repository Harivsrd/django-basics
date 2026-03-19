from django.shortcuts import render
from django.db import transaction
from django.db.models import Q , F , Value , Func , Count , ExpressionWrapper , DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product , OrderItem , Order , Customer, Collection
from tags.models import TaggedItem
from django.core.exceptions import ObjectDoesNotExist

# @transaction.atomic()
def say_hello(request):
    #Products : inventory < 10 AND price < 20
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20) )              
    #compoaring two fileds like inventory = unit_price... which is not possible -- F - objects
    # queryset = Product.objects.filter(inventory=F('collection__id'))
    # queryset = Product.objects.order_by('title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')
    
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values('id','title')
    # queryset = Product.objects.values('id','title','collection__title')
    
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Product.objects.only('id','title')
    # queryset = Product.objects.defer('description')
    # queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    # result = Product.objects.aggregate(count=Count('id'), min_price= Min('unit_price'))
    
    # queryset = Customer.objects.annotate(new_id = Value(True))
    # queryset = Customer.objects.annotate(new_id = F('id')+1)
    # queryset = Customer.objects.annotate(
    #     #CONCAT 
    #     full_name = Func(('first_name') ,Value(' '), F('last_name'),function='CONCAT')
    # )
    
    # queryset = Customer.objects.annotate(
    #     #CONCAT 
    #     full_name = Concat('first_name', Value(' '),0 'last_name')
    # )
    # queryset = Customer.objects.annotate(
    #     #CONCAT 
    #     orders_count = Count('order')
    # )
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     #CONCAT 
    #     discounted_price = discounted_price
    # )
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects \
    # .select_related('tag')\
    # .filter(
    #     content_type=content_type,
    #     object_id = 1
    # )
    
    # TaggedItem.objects.get_tags_for(Product, 1)
    
    # queryset = Product.objects.all()
    # list(queryset)
    # list(queryset)
    
    # collection = Collection()
    # collection.name = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    # collection.id 
    
    # collection = Collection.objects.create(name='a', featured_product_id=1)
    # collection.id
    
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()
    
    # Collection.objects.filter(pk=11).update(featured_product=None)
    
    # Collection.delete()
    
    # Collection.objects.filter(id__gt=5).delete()
    
    
    with transaction.atomic():
        
        order = Order() 
        order.customer_id = 1
        order.save()
        
        item = OrderItem()
        item.order = order 
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    
    return render(request, 'hello.html', {'name': 'max'})
