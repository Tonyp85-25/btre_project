from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Following
from django.contrib import messages
# Create your views here.


@login_required
def follow(request):
    """
    allows user to follow a listing
    """
    if request.method == 'POST':
        user_id = request.user.id
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        following = Following(user_id=user_id, listing_id=listing_id, listing=listing)
        has_followed = Following.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_followed:
            return redirect('/listings/' + listing_id)
        else:
            following.save()

        return redirect('/listings/' + listing_id)


@login_required
def unfollow(request):
    """
    allows user to remove listing's following
    """
    user_id = request.user.id
    listing_id = request.POST['listing_id']
    following = Following.objects.all().filter(listing_id=listing_id, user_id=user_id)
    if following:
        following.delete()
    return redirect('/listings/' + listing_id)
