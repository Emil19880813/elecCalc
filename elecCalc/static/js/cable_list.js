$(function () {
    var down = $(".arrow-down");
    var up = $(".arrow-up");

    down.each(function (index, el) {
        $(this).on("click", function(event) {
            event.preventDefault();
            tr = $(this).parent().parent().parent();
            $.post('/position/',
                {
                    pos_nr: tr.data('position')

                }).done(function (data) {
                    if (data['status'] == 'ok')
                    {
                        var next_tr = tr.next();
                        var move = tr.detach();
                        move.insertAfter(next_tr);
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
