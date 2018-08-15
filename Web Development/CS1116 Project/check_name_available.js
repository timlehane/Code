(function() {
    
    var username;
    var checker;
    var request;
    
    document.addEventListener('DOMContentLoaded', init, false);

    function init() {
        username = document.querySelector('#username');
        checker = document.querySelector('#checker');
        username.addEventListener('keypress', set_link, false);
        checker.addEventListener('click', check_name_available, false);
    }

    function set_link() {
        checker.innerHTML = '<a href="#">Check name is available</a>';
    }

    function check_name_available() {
        var url = 'check_name_available.py?username=' + username.value;
        request = new XMLHttpRequest();
        request.addEventListener('readystatechange', handle_response, false);
        request.open('GET', url, true);
        request.send(null);
    }
    
    function handle_response() {
        // Check that the response has fully arrived
        if ( request.readyState === 4 ) {
            // Check the request was successful
            if ( request.status === 200 ) {
                if ( request.responseText.trim() === 'available' ) {
                    checker.innerHTML = 'Name available';
                } else if ( request.responseText.trim() === 'in_use' ) {
                    checker.innerHTML = 'Name not available';
                }
            }
        }
    }

})();