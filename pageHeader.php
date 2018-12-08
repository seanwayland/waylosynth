<?php
/**
 * Created by PhpStorm.
 * User: sean
 * Date: 10/17/18
 * Time: 8:10 PM
 */

/** BASIC PAGE HEADER  */


/* Displays user information and some useful messages */
require 'db.php';
session_start();


// Check if user is logged in using the session variable
if ( $_SESSION['logged_in'] != 1 ) {
    $_SESSION['message'] = "You must log in before viewing your profile page!";
    header("location: error.php");
}
else {
    // Makes it easier to read
    $first_name = $_SESSION['first_name'];
    $last_name = $_SESSION['last_name'];
    $email = $_SESSION['email'];
    $active = $_SESSION['active'];
    $result = $mysqli->query("SELECT * FROM users WHERE email='$email'");
    $user = $result->fetch_assoc();
    $credits = $user['credits'];


}
?>
    <!DOCTYPE html>
    <html >
    <style>
        body {
            background: #D3D3D3D3; /* #c1bdba */

            font-family: 'Titillium Web', sans-serif;
        }


        /* The navigation bar */
        .navbar {
            position: fixed; /* Set the navbar to fixed position */
            top: 0px;
            left: 600px;
            width: 100%; /* Full width */
        }

        input[type=text] {
            background-color: white;
            color: black;
        }

        a:link {
            color: #1ab188;
        }

        /* visited link */
        a:visited {
            color: blue;
        }

        /* mouse over link */
        a:hover {
            color: green;
        }

        /* selected link */
        a:active {
            color: greenyellow;
        }


        button {
            background-color: #1ab188; /* Green */
            border: none;
            color: black;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
        }

        img {
            width: 30%;
            height: 30%;

        }

    </style>
    <head>
        <meta charset="UTF-8">
        <title>WAYLOSTREAMS.COM <?= $first_name.' '.$last_name?></title>

    </head>

<body>
<div class="form">



    <br>

    <img src="waylostreams.jpg" alt="WAYLOSTREAMS">





    <p>
        <?php

        // Display message about account verification link only once
        if ( isset($_SESSION['message']) )
        {
            echo $_SESSION['message'];

            // Don't annoy the user with more messages upon page refresh
            unset( $_SESSION['message'] );
        }

        ?>
    </p>

    <?php

    // Keep reminding the user this account is not active, until they activate
    if ( !$active ){
        echo
        '<div class="info">
              Account is unverified, please confirm your email by clicking
              on the email link!
              </div>';
    }

    ?>

    <h2><?php echo "Hello ", $first_name.' '.$last_name; ?></h2>
    <p><?= $email ?></p>


    <div class="navbar">

        <br />
        WWW.WAYLOSTREAMS.COM
        <br />

    <a href="logout.php"><button class="button button-block" name="logout"/>Log Out</button></a>

        <br />
        <a href="http://www.waylostreams.com/login-system/profile.php">Go back to profile page </a>
        <br />


    </div>

</div>

<br />
<br />
<br />

<?php

echo "You have: ";
echo $credits;
echo " credits";
echo "<br>";
$song_id = 1;

// fetch the logged in users email
$email = $mysqli->escape_string($_SESSION['email']);
$result = $mysqli->query("SELECT * FROM users WHERE email='$email'");
$user = $result->fetch_assoc();
$user_id = $user['id'];


?>