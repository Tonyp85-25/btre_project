from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Following
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


@login_required
def follow(request):
    """
    allows user to follow a listing
    """
    if request.method == 'POST' and request.is_ajax:
        user_id = request.user.id
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        following = Following(user_id=user_id, listing_id=listing_id, listing=listing)
        has_followed = Following.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_followed:
            return JsonResponse({"message": "You already follow this listing!", "result": "error", "class": "danger"}, status=200)
        else:
            following.save()

        return JsonResponse({"message": "You now follow this listing!", "result": "success", "class": "success"}, status=200)


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
