const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$('#followForm').on('submit', function(e){
    e.preventDefault();
    let formData = $(this).serialize();
    addToFav(formData);
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
            console.log (obj);
            displayMessages([obj]);

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