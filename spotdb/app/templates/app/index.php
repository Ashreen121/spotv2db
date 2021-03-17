{% load static %}
{% load scrapy %}

<?php
/**
 * This is an example of how to authenticate a user with a University username
 * and password.
 * 
 * It required the instillation of the file Authenticator.php in the same 
 * directory.
 * 
 * @todo The developer must edit this file to define the constant DEVELOPER_URL.
 * 
 * @author Iain Hart (iain@cs.man.ac.uk)
 * @date 1st November 2013
 */

// @todo Replace the following defined constant with the URL which runs the 
// program requiring authentication.
define ("DEVELOPER_URL", "http://localhost/app/");

// Define the location of the service on the Computer Science server.
define("AUTHENTICATION_SERVICE_URL", "http://studentnet.cs.manchester.ac.uk/authenticate/");

// Define the location of CAS's logtout service on the Computer Science server.
define("AUTHENTICATION_LOGOUT_URL", "http://studentnet.cs.manchester.ac.uk/systemlogout.php");

// Locate the Authenticator class.
require_once("Authenticator.php");

// Start a php session to store variables. This will be used to hold the ticket
// issued to the user so that when the user returns from CAS we know that
// we are interacting with the same user.
session_start();

// Uncomment this next line if study year is required but this will necessitate
// an extra query on the database so only use it if genuinely needed.
// Authenticator::requireStudyLevel();

// Validate the user.
Authenticator::validateUser();

// To invalidate a user uncomment the following. It uses header() to send the
// user to CAS's logout page on the Computer Science server. To work you must
// not have returned any output to the client before calling it.

// Authenticator::invalidateUser();

?>


<!DOCTYPE html>
<html lang="en">

  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    

    <!-- Bootstrap CSS using cdn -->
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"> -->
    <!-- Bootstrap CSS using source files -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">

    <title>SPOTv2</title>
  </head>


  <body>
    <div class="bckgrd">
      <div class="main">
        <h1 class="titlespot">SPOT v2</h1>
        <div id="id_div">
            {% scrape_now 'Foo' as success_message %}
            <strong> {{ success_message }} </strong>
        </div>
        <form action="/action_page.php">
          <div class="row">
            <div class="col-1">
              <i class="fas fa-user p-3"></i>
            </div>
            <div class="col">
              <div class="form-group"> 

                <input type="username" class="form-control" id="username" placeholder="UoM username" name="username" required>
                
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-1">
              <i class="fas fa-key p-3"></i>
            </div>
            <div class="col">
              <div class="form-group">
                <input type="password" class="form-control" id="pwd" placeholder="Enter UoM password" name="pswd" required>
              </div>
            </div>
            
          </div>
          <div class="row">
            <div class="col-1"></div>
            <div class="col"> 
              <div class="form-group form-check">
            <label class="form-check-label p-3">
              <input class="form-check-input" type="checkbox" name="remember"> Remember me
            </label>
          </div>
          <li>
              Your username is 
                  <?php
                      echo Authenticator::getUsername();
                  ?>
          </li>

          <button href="http://127.0.0.1:8000/deadlines" type="submit" class="btn btn-primary">Log In</button></div>
          </div>
         
        </form>
      </div>
    </div>   
  </body>

</html>



<style>
  @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
  html, body {
    height: 100%;
     margin: 0;
  }

  .main {
    position: fixed;
    width: 50%;
    top: 21%;
    left: 23%;
  }

  .titlespot {
    position: relative;
    width: 50%;

    font-family: 'Fredoka One', cursive;;
    font-style: normal;
    font-weight: normal;
    font-size: 500%;
    line-height: 80%;
    /* identical to box height */

    text-align: center;

    color: #FFFFFF;
  }

  .bckgrd {
    background: linear-gradient(65.61deg, #6EC4DF 2.78%, #1D79D3 84.25%);

    height: 100%; 

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
  }
  
  .blue {
    color:rgb(0, 162, 255);
  }
</style>
