const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$('#followForm').on('submit', function(e){
    e.preventDefault();
    let formData = $(this).serialize();
    if($('#follow').hasClass('btn-sucess'))
    {
        addToFav(formData);
    }
    else{
        removeFromFav(formData);
    }

});

function addToFav(pData)
{
    let route = $('#follow').data('url');
    $.ajax({
        url: route,
        dataType: 'json',
        method: 'POST',
        data: pData,
        success: function(obj){
            console.log('success');
            displayMessages([obj]);
            toggleButton('unfollow');
            $('#follow').data('url', obj.route);


        },
        error: function(xHR,status, error){
            console.log(xHR,status,error);
        }

    });
}

function displayMessages(messages)
{
    let html = []
    messages.forEach(function(m, index)
    {
        let div = `<div class="alert alert-${m.class} alert-dismissible text-center" >`;
        div += '<button type="button" class="close" data-dismiss="alert" aria-hidden="true"><span>&times;</span></button>';
        div+= `<strong>${m.result}!</strong>`;
        div += ` ${m.message}</div>`;
        html.push(div);
    })
   $('div.messages').append(html.join('\n'));
}

function toggleButton(pAction)
{
    if (pAction == 'unfollow') {
          $('#follow').removeClass('btn-success');
        $('#follow').addClass('btn-danger');
         $('#follow i').removeClass('fa-plus-circle');
        $('#follow i').addClass('fa-minus-circle');
        $('#follow').text('Remove from favorites');
    } else{
         $('#follow').removeClass('btn-danger');
        $('#follow').addClass('btn-success');
         $('#follow i').removeClass('fa-minus-circle');
        $('#follow i').addClass('fa-plus-circle');
        $('#follow').text('Add to favorites');
    }

}

function removeFromFav(pData)
{
    let route = $('#follow').data('url');
    $.ajax({
        url: route,
        dataType: 'json',
        method: 'POST',
        data: pData,
        success: function(obj){
            console.log('success');
            displayMessages([obj]);
             toggleButton('follow');
            $('#follow').data('url', obj.route);

        },
        error: function(xHR,status, error){
            console.log(xHR,status,error);
        }

    });
}