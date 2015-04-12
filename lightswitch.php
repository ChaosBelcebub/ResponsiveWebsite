	

    <?php
     
    // Überprüfen ob 'room' übergeben wurde:
    if(empty($_GET['room'])) {
        http_response_code(400);
        exit(0);
    }
     
    // Setzen der Variable room mit der RaumID
    $room = $_GET['room'];
     
    // Überprüfen welcher Wert room hat
    if($room == 'room1') {
        toggle_power(1);
    }
    elseif($room == 'room2') {
        toggle_power(2);
    }
    else {
        http_response_code(400);
        exit(0);
    }

