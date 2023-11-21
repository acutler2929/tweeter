//  Alice Cutler
//  CIS 218
//  November 20, 2023
$(document).ready(function () {
    $('.like_button').click(function (event) {
        // Get required data
        let target = $(event.currentTarget);
        let tweet_id = target.data('id');
        let tweet_action = target.data('action');
        let tweet_like_url = target.data('like_url');

        // Get icon and count elements
        let like_icon = target.find('like_icon');
        let like_count = target.find('like_count');

        $.ajax({
            url: tweet_like_url,
            data: {
                tweet_id: tweet_id,
                tweet_action: tweet_action,
            },
        }).done(function (data) {
            // When complete, check to see it was successful
            if (data.success) {
                // If liked, update elements to match
                if (article_action === 'like') {
                    target.data('action', 'unlike');
                    target.removeClass('btn-outline-primary');
                    target.addClass('primary');
                    like_icon.removeClass('bi-hand-thumbs-up');
                    like_icon.addClass('bi-hand-thumbs-up-fill');
                    like_count.html(Number(like_count.html() + 1));
                } else {
                    // Else, update elements to match unlike
                    target.data('action', 'like');
                    target.removeClass('btn-primary');
                    target.addClass('btn-outline-primary');
                    like_icon.removeClass('bi-hand-thumbs-up-fill');
                    like_icon.addClass('bi-hand-thumbs-up');
                    like_count.html(Number(like_count.html() - 1));
                }
            }
        });
    });
});