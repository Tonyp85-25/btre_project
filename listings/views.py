from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Listing
from .choices import bedrooms_choices, states_choices, prices_choices
from  followings.models  import Following


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':  paged_listings,

    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    user_id = request.user.id
    listing = get_object_or_404(Listing, pk=listing_id)
    l_range = ['1','2','3','4','5','6']
    following = Following.objects.all().filter(listing_id=listing_id, user_id=user_id)
    if following:
        is_followed = True
    else:
        is_followed = False

    context = {
        'listing': listing,
        'l_range': l_range,
        'is_followed': is_followed
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['keywords']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context = {
        'states_choices': states_choices,
        'bedrooms_choices': bedrooms_choices,
        'prices_choices': prices_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)


