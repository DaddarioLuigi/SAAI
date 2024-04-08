$(document).ready(function() {
    $('#send-btn').click(function() {
        let userInput = $('#user-input').val();
        if (userInput.trim() != '') {
            $('#chat-box').append('<div class="user-message">' + userInput + '</div>');

            // Clear input box
            $('#user-input').val('');

            // Call the API
            $.ajax({
                url: '/process', // Flask route that will handle the API call
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ message: userInput }),
                success: function(response) {
                    $('#chat-box').append('<div class="bot-response">' + response + '</div>');
                    // Scroll to the bottom of the chat box
                    $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
                }
            });
        }
    });
});
