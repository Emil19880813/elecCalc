$(function () {

    $.ajaxSetup({
        headers: { "X-CSRFToken": $.cookie("csrftoken") }
    });

    var down = $(".arrow-down");
    var up = $(".arrow-up");

    down.each(function (index, el) {
        $(this).on("click", function(event) {
            event.preventDefault();
            tr = $(this).parent().parent().parent();
            $.post('/position/',
                {
                    pos_nr: tr.data('id'),

                }).done(function (data) {
                    if (data['status'] == 'ok')
                    {
                        var next_tr = tr.next();
                        var move = tr.detach();
                        move.insertAfter(next_tr);

                        var td = $(this).parent().parent().next().html();
                        var next_td = next_tr.parent().parent().next().html();
                        td.html(function (i, next_td) {
                            return next_td
                        });
                        next_td.html(function (i, td) {
                            return td
                        });
                    }
                }
            );
        });
    });

    up.each(function (index, el) {
        $(this).on("click", function(event) {
            event.preventDefault();
            var tr = $(this).parent().parent().parent();
            var prev_tr = tr.prev();
            var move = tr.detach();
            move.insertBefore(prev_tr);
        });
    });

});
