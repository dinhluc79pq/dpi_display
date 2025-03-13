$(document).ready(function() {
    $('#search').on('click', function(){
        search()
    })

    $('#refresh').on('click', function() {
        $('#img').html('')
    })

    function search() {
        message = 'Đang load ảnh ...'
        $('#message').text(message)
        numberImg = $('#numberSearch').val()
        $.ajax({
            type: "POST",
            url: "/getImages",
            data: JSON.stringify({numberImg: numberImg}),
            contentType: 'application/json',
            success: function (response) {
                if (!response.result) {
                    $('#img').append('<img class="background-img" src="' + response.background1 + '">')
                    $('#img').append('<img class="background-img" src="' + response.background2 + '">')
                    $('#img').append('<img class="background-img" src="' + response.background3 + '">')
                    $('#img').append('<img class="background-img" src="' + response.background4 + '">')
                    $('#message').text('')   
                }
                else {
                    $('#message').text('Không tìm thấy số ảnh vừa nhập vào!')   
                }
                
            }
        });
    }


    $("#numberSearch").keypress(function(event) {
        if (event.keyCode === 13) {
            search()
        }
    })
});
