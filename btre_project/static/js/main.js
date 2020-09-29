const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$('#follow').on('click', function(){
    addToFav();
});

function addToFav() {
    let userId = $('input[name="user_id"]').val();
    let listingId = $('input[name="listing_id"]').val();
    let listing = $('input[name="listing"]').val();

    $.ajax({
        url: '/followings/follow',
        dataType: 'json',
        method: 'POST',
        data: {user_id: userId, listing_id:listingId, listing: listing},
        success: function(obj){
            console.log('success');
            console.log (obj);
        },
        error: function(xHR,status, error){
            console.log(xHR,status,error)
        }

    });
}