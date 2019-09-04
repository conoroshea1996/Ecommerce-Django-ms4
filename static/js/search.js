$(document).on('submit', '.test', function (e) {
    console.log(e);
    var form = $('.test')
    event.preventDefault()
    var thisForm = $(this);
    var actionEndpoint = thisForm.attr('action');
    var httpMethod = thisForm.attr('method');

    console.log(thisForm.attr('action'), thisForm.attr('method'));

    $.ajax({
        url: actionEndpoint,
        type: 'GET',
        data: {
            'q': $('#search').val(),
            'num': 1,
        },
        success: function (data) {
            var x = $(data).find("#products-list").html();
            $('#products-list').html(x);
            console.log(data);
            console.log(x);
        },
        dataType: 'html',
        error: function (errorData) {
            console.log('doesnt work', errorData);

        }
    })
})

$(document).on('change', '.filter-catagory', function (e) {
    console.log(e);
    var data = $('input[name=catagory]:checked').serializeArray();

    $.ajax({
        url: '/products/',
        type: 'GET',
        data: data,
        success: function (data) {
            var x = $(data).find("#products-list").html();
            $('#products-list').html(x);
        },
        dataType: 'html',
        error: function (errorData) {
            console.log(errorData);

        }
    })
})


$(document).ready(function () {
    $('#div_id_product').hide()
})

$(document).on('submit', '#comments', function (e) {
    event.preventDefault();
    var data = $('#comments').serializeArray();
    var key = $('.id_pk_key').text()

    data[3].value = key;
    var prod_id = data[3].value;
    $.ajax({
        url: `/products/${prod_id}/`,
        type: 'POST',
        data: data,
        success: function (data) {
            var success = $($.parseHTML(data)).filter(".comment-section-box");
            var comments_form = $($.parseHTML(data)).filter("#comments");
            $('#comments').replaceWith(comments_form);
            $('.comment-section-box').replaceWith(success);
            $('#div_id_product').hide()
        },
        error: function (errorData) {
            console.log(errorData);
        },
        timeout: 5000 // sets timeout to 5 seconds
    })
})


//  Alert message disaper after 3 seconds

setTimeout(function () {
    $('.alert').slideUp('slow')
}, 3000)