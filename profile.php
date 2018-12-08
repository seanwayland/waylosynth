<?php
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


    // <p><?= $email
}
?>
<!DOCTYPE html>
<html >
<!--HTML page formatting -->
<style>
    body {
        background: #D3D3D3D3; /* #c1bdba */
        font-family: 'Titillium Web', sans-serif;
    }

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

    /* unvisited link */
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


    <br />

</head>

<body>



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
              on the email link! You cannot buy credits or redeem free credits without verifying.
              </div>';
}

?>

<?php echo "Hello ", $first_name.' '.$last_name; ?>



<br />
<br />
<br />


BUY 10,000 CREDITS for US $10 with PAYPAL


<form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
    <input type="hidden" name="cmd" value="_s-xclick"><input type="hidden" name="hosted_button_id" value="E9V2SAV7HS668"><input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_cart_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
</form>




<br />
<br />



<a href="http://www.waylostreams.com/login-system/freecredits.php">click here to get 10 free credits for new users</a>
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

// grab the song purchase cost from the songs table

$song_id = $mysqli->escape_string($song_id);
$result = $mysqli->query("SELECT * FROM songs WHERE id='$song_id'");
$song = $result->fetch_assoc();
$purchase_cost = $song['purchase_cost'];

// this code below a sticks up an html audio player and calls the source file
// from the database. It selects the URL of the source and then
// streams the file secretly

?>




<div class="form">
    <a>
        <form action="searchResult.php" method="post">
            <div class="field-wrap">
                <p>Search Artists:  <input type="text" name="name" /></p>

                <p><input type="submit" /></p>
            </div>
        </form>


        <form action="searchResultAlbums.php" method="post">
            <p>Search Albums: <input type="text" name="name" /></p>

            <p><input type="submit" /></p>
        </form>

        <form action="searchResultSongs.php" method="post">
            <p>Search Songs:  <input type="text" name="name" /></p>

            <p><input type="submit" /></p>
        </form>

        <form action="searchAlbumCredits.php" method="post">
            <p>Search Album Credits:  <input type="text" name="name" /></p>

            <p><input type="submit" /></p>
        </form>




</div>


<br />



<a href="http://www.waylostreams.com/login-system/artistArea.php">artists click here to upload music </a>
<br />



</body>


<div class="navbar">

    <br />
    WWW.WAYLOSTREAMS.COM
    <br />

    <a href="logout.php"><button class="button button-block" name="logout"/>Log Out</button></a>

    <br />
    <a href="http://www.waylostreams.com/login-system/profile.php">Go back to profile page </a>
    <br />


</div>

</html>