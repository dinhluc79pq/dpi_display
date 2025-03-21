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
                    let html = `
                        <span class="num-title title">${numberImg}</span>
                        <img class="background-img" src="${response.background1}">
                        <span class="num-title title">${numberImg}</span>
                        <img class="background-img" src="${response.background2}">
                        <span class="num-title title">${numberImg}</span>
                        <img class="background-img" src="${response.background3}">
                        <span class="num-title title">${numberImg}</span>
                        <img class="background-img" src="${response.background4}">
                    `
                    $('#img').append(html)
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
