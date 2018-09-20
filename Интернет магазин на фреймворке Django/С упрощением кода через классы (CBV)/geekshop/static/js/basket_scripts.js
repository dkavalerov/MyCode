window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var inputObject = event.target;

        $.ajax({
            url: "/basket/edit/" + inputObject.name + "/" + inputObject.value + "/",

            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });

        event.preventDefault();
    });
}