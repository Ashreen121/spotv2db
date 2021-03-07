{% load static %}

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
define ("DEVELOPER_URL", "http://localhost/app/deadlines.php");

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
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap" rel="stylesheet">
    <title>SPOTv2</title>
  </head>
  <!-- Arbitrary id to give it more priority to overide some Bootstrap stylings -->
  <body id="bootstrap-overide">
    <div>
      <span class="material-icons login">account_circle</span>
    </div>
    <div id="object-center">
      <h1>SPOT v2</h1>
      <div class="form-outline">
        <input type="search" id="form1" class="form-control" placeholder="Search for Courses" aria-label="Search"/>
      </div>
      <table class="table table-borderless">
        <colgroup>
          <col class="course" span="1">
          <col class="course-info" span="2">
        </colgroup>
        <thead>
          <tr id="table-head">
            <th id="cell-topleft" scope="col">Courses</th>
            <th scope="col">Assignments</th>
            <th id="cell-topright" scope="col">Due Dates</th>
          </tr>
        </thead>
        <tbody class="course-row">
          <tr>
            <th scope="row" rowspan="3">COMP#####</th>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
        </tbody>
        <tbody class="course-row">
          <tr>
            <th scope="row" rowspan="3">COMP#####</th>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
        </tbody>
        <tbody class="course-row">
          <tr>
            <th scope="row" rowspan="3">COMP#####</th>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
        </tbody>
        <tbody class="course-row">
          <tr>
            <th scope="row" rowspan="3">COMP#####</th>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
        </tbody>
        <tbody class="course-row">
          <tr>
            <th scope="row" rowspan="3">COMP#####</th>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
        </tbody>
        <tbody class="course-row">
          <tr>
            <th id="cell-bottomleft" scope="row" rowspan="3">COMP#####</th>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td>dd/mm/yyyy</td>
          </tr>
          <tr>
            <td>Assignment #</td>
            <td id="cell-bottomright">dd/mm/yyyy</td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>

<style media="screen">

body{
  /* I have no idea why the code below doesn't give me a gradient, please help */
  /* background: linear-gradient(to left, #1976D2 0%, #6ec4de 100%); */
  background: #1976D2;
}

.material-icons.login{
  color: white;
  font-size: 48px;
  position: absolute;
  right: 5%;
  top: 5%;
}

#object-center{
  position: absolute;
  top: 10%;
  left: 10%;
  right: 10%;
}

h1{
  font-family: 'Fredoka One', cursive;
  font-size: 60px;
  color: white;
}

#form1{
  border-radius: 33px;
  background: #E3F2FD;
  border: 4px solid white;
  font-family: 'Comfortaa', cursive;
}

.table, #bootstrap-overide th, #bootstrap-overide td{
  line-height: 5px;
  font-family: 'Comfortaa', cursive;
  text-align: center;
  vertical-align: middle;
  border-collapse: separate;
  border-spacing: 0px;
  margin-top: 25px;
}

td{
  font-size: 12px;
}

thead{
  background: linear-gradient(to left, #1976D2 0%, #6ec4de 100%);
  border-top-left-radius: 33px;
}

tbody{
  background: #c9f1fd;
}

#bootstrap-overide thead th{
  line-height: 40px;
  border-top: 4px solid white;
  color: white;
}

/* This is the only way I could find to make bordered tables. I'm sorry */
/* It looks weird on Firefox, but should work on Chrome and Edge. Will fix later */
th, td{
  border-right: 4px solid white;
}

#bootstrap-overide th,
#bootstrap-overide tbody.course-row tr:last-child td{
  border-bottom: 4px solid white;
}

th:first-child{
  border-left: 4px solid white;
}

#cell-topleft{
  border-top-left-radius: 33px;
}

#cell-topright{
  border-top-right-radius: 33px;
}

#cell-bottomleft{
  border-bottom-left-radius: 33px;
}

#cell-bottomright{
  border-bottom-right-radius: 33px;
}
</style>
