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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <title>SPOTv2</title>
  </head>



  <!-- Arbitrary id to give it more priority to overide some Bootstrap stylings -->
  <body id="bootstrap-overide">
    <div class="row">
      <div class="col-sm-3">
        <section class="timeline">
          <ul id = 'ul'>
            
            <!-- more list items here -->
            {% for assignment in assignmentList %}



                <li id="li">
                  <div id="div">
                    <time>{{assignment.DateDue}}</time>
                    <p> {{assignment.Course}} </p>
                    <p> {{assignment}} </p>
                  </div>
                </li>
            {% endfor %}


          </ul>

            

        </section>
      </div>
      <div class="col-sm-9 bckgrd">
        <div>
          <span class="material-icons login">account_circle</span>
        </div>
        <div id="object-center">
          <h1>SPOT v2</h1>
          <div class="form-outline">
            <input type="search" id="form1" class="form-control" placeholder="Search for Courses" aria-label="Search"/>
          </div>
          <table class="table table-borderless" style="margin-bottom: 0;">
            <colgroup>
              <col class="course" span="1">
              <col class="course-info" span="2">
            </colgroup>
            <thead>
              <tr id="table-head">
                <th id="cell-topleft" scope="col" , style="width: 33%;">Courses</th>
                <th scope="col" , style="width: 33%;">Assignments</th>
                <th id="cell-topright" scope="col" , style="width: 33.5%;">Due Dates</th>
              </tr>
            </thead>
          </table>
          <div class="tablelocker ", id = "packageThing">
            <table id="table" class="table table-borderless" style="margin: 0;">
              <colgroup>
                <col class="course" span="1">
                <col class="course-info" span="2">
              </colgroup>
              {% for key, value in items.items %}
                <tbody class="course-row">

                {% for assignment in value %}
                  {% if forloop.counter == 1 %}
                  <tr>
                    <th scope="row" rowspan="{{ value|length }}" style="width: 33%;">{{key}}</th>
                    <td style="width: 33%;">{{assignment}}</td>
                    <td style="width: 33%;">{{assignment.DateDue}}

                      <div class="dropdown" style="float: right;">

                          <button type="button" class="btn btn-info dropdown-toggle" data-toggle="dropdown" style="margin: 0; background: #1976D2; width: 3vw; font-size: 100%; color: white;">
                            <i class="fa fa-calendar-plus-o"></i>
                          </button>

                          <div class="dropdown-menu">
                            <a class="dropdown-item" href="https://outlook.office.com/calendar/0/deeplink/compose?body={{key}}%20{{assignment}}&enddt={{assignment.DateDue}}&location=N%2FA&path=%2Fcalendar%2Faction%2Fcompose&rru=addevent&startdt={{assignment.DateDue}}&subject={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Outlook.com</a>
                            <a class="dropdown-item" href="https://calendar.google.com/calendar/render?action=TEMPLATE&dates={{assignment.DateDue}}%{{assignment.DateDue}}&details={{key}}%20{{assignment}}&location=N%2FA&text={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Google</a>
                          </div>

                        </div>

                    </td>
                  </tr>

                  {% elif forloop.parentloop.counter == items|length and forloop.counter == 1 %}
                  <tr>
                    <th scope="row" rowspan="{{ value|length }}" style="width: 33%;">{{key}}</th>
                    <td style="width: 33%;">{{assignment}}</td>
                    <td style="width: 33%;">{{assignment.DateDue}}
                      <div class="dropdown" style="float: right;">

                          <button type="button" class="btn btn-info dropdown-toggle" data-toggle="dropdown" style="margin: 0; background: #1976D2; width: 3vw; font-size: 100%; color: white;">
                            <i class="fa fa-calendar-plus-o"></i>
                          </button>

                          <div class="dropdown-menu">
                            <a class="dropdown-item" href="https://outlook.office.com/calendar/0/deeplink/compose?body={{key}}%20{{assignment}}&enddt={{assignment.DateDue}}&location=N%2FA&path=%2Fcalendar%2Faction%2Fcompose&rru=addevent&startdt={{assignment.DateDue}}&subject={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Outlook.com</a>
                            <a class="dropdown-item" href="https://calendar.google.com/calendar/render?action=TEMPLATE&dates={{assignment.DateDue}}%{{assignment.DateDue}}&details={{key}}%20{{assignment}}&location=N%2FA&text={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Google</a>
                          </div>

                        </div>
                    </td>
                  </tr>

                  {% elif forloop.parentloop.counter == items|length and forloop.counter == value|length %}
                  <tr>
                    <td>{{assignment}}</td>
                    <td id="cell-bottomright">{{assignment.DateDue}}
                      <div class="dropdown" style="float: right;">

                          <button type="button" class="btn btn-info dropdown-toggle" data-toggle="dropdown" style="margin: 0; background: #1976D2; width: 3vw; font-size: 100%; color: white;">
                            <i class="fa fa-calendar-plus-o"></i>
                          </button>

                          <div class="dropdown-menu">
                            <a class="dropdown-item" href="https://outlook.office.com/calendar/0/deeplink/compose?body={{key}}%20{{assignment}}&enddt={{assignment.DateDue}}&location=N%2FA&path=%2Fcalendar%2Faction%2Fcompose&rru=addevent&startdt={{assignment.DateDue}}&subject={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Outlook.com</a>
                            <a class="dropdown-item" href="https://calendar.google.com/calendar/render?action=TEMPLATE&dates={{assignment.DateDue}}%{{assignment.DateDue}}&details={{key}}%20{{assignment}}&location=N%2FA&text={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Google</a>
                          </div>

                        </div>
                    </td>
                  </tr>


                  {% else %}
                  <tr>
                    <td>{{assignment}}</td>
                    <td>{{assignment.DateDue}}
                      <div class="dropdown" style="float: right;">

                          <button type="button" class="btn btn-info dropdown-toggle" data-toggle="dropdown" style="margin: 0; background: #1976D2; width: 3vw; font-size: 100%; color: white;">
                            <i class="fa fa-calendar-plus-o"></i>
                          </button>

                          <div class="dropdown-menu">
                            <a class="dropdown-item" href="https://outlook.office.com/calendar/0/deeplink/compose?body={{key}}%20{{assignment}}&enddt={{assignment.DateDue}}&location=N%2FA&path=%2Fcalendar%2Faction%2Fcompose&rru=addevent&startdt={{assignment.DateDue}}&subject={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Outlook.com</a>
                            <a class="dropdown-item" href="https://calendar.google.com/calendar/render?action=TEMPLATE&dates={{assignment.DateDue}}%{{assignment.DateDue}}&details={{key}}%20{{assignment}}&location=N%2FA&text={{assignment}}" target="_blank" style="text-decoration-line: none; background-color: #1976D2; color: white; font-family: Comfortaa; padding: 1vw; filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));">Google</a>
                          </div>

                        </div>
                    </td>
                  </tr>
                  {% endif %}


                {% endfor %}

                </tbody>
              {% endfor %}
            </table>

          </div>
           
          </table>
          <a href="https://campaigns.litmus.com/_email/test/newnewyork.ics" class="btn btn-info" style=""><span style="mso-text-raise:15pt;"><i class = "fa fa-calendar-plus-o"></i> Add  all to your Calendar</span></a>

        </div>
      </div>
      
    </div>
    
    <script>
      $(document).ready(function(){
        $("#form1").on("keyup", function() {
          var value = $(this).val().toLowerCase();
          $("#table tbody").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
          });
        });
      });
    </script>

  </body>
</html>

<style media="screen">
  .row {
    width: 100%;
    margin: 0;
    overflow-y:auto;
    display: flex;
    height: 100vh;
    

  }
  .col {
    margin: 0;
  }
  .col-sm-9 {
    padding-left: 10%;
    padding-right: 10%;
    padding-top: 2%;
    padding-bottom: 5%;

  }
  .col-sm-3 {
    box-shadow: inset -4px 0px 4px rgba(0, 0, 0, 0.25);
    padding-right: 2%;
    height: 100vh;
    overflow-y: auto;

  }

  .timeline {
    font: normal 16px/1.5 "Helvetica Neue", sans-serif;
    background: #FFFFFF;
    color: #fff;
    overflow-x: hidden;
    
  } 

  .timeline ul li {
    list-style-type: none;
    position: relative;
    width: 6px;
    margin: 0 auto;
    margin-left: 50px;
    padding-top: 50px;
    background: #6EC4DF;
  }
   
  .timeline ul li::after {
    content: '';
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: inherit;
  }

  .timeline ul li div {
    position: relative;
    bottom: 0;
    width: 400px;
    padding: 15px;
    background: linear-gradient(65.61deg, #6EC4DF 20.78%, #1D79D3 96.25%);
  }
   
  .timeline ul li div::before {
    content: '';
    position: absolute;
    bottom: 7px;
    width: 0;
    height: 0;
    border-style: solid;
  }

  .timeline ul li:nth-child(odd) div {
    left: 45px;
  }
   
  .timeline ul li:nth-child(odd) div::before {
    left: -15px;
    border-width: 8px 16px 8px 0;
    border-color: transparent #6EC4DF transparent transparent;
  }

  .timeline ul li:nth-child(even) div {
    left: 45px;
  }
   
  .timeline ul li:nth-child(even) div::before {
    left: -15px;
    border-width: 8px 16px 8px 0;
    border-color: transparent #6EC4DF transparent transparent;
  }

  .bckgrd {
    background: linear-gradient(65.61deg, #6EC4DF 2.78%, #1D79D3 84.25%);
    height: 100%; 
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    margin: 0;
  }


  .material-icons.login{
    float: right;
    color: white;
    font-size: 300%;
    right: 5%;
    top: 5%;
  }



  h1{
    font-family: 'Fredoka One', cursive;
    font-size: 500%;
    color: white;
  }

  #form1{
    border-radius: 33px;
    background: #E3F2FD;
    border: 4px solid white;
    font-family: 'Comfortaa', cursive;
    box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
  }

  .tablelocker {
    height: 45vh;
    overflow-y: auto;
    border-bottom: 4px solid white;
    box-shadow: 3px 3px 4px rgba(0, 0, 0, 0.25);
  }

  .table, #bootstrap-overide th, #bootstrap-overide td{
    line-height: 60%;
    font-family: 'Comfortaa', cursive;
    text-align: center;
    vertical-align: middle;
    margin-top: 10px;
  }

  td{
    font-size: 70%;
  }

  thead{
    background: linear-gradient(to left, #1976D2 0%, #6ec4de 100%);
  }

  tbody{
    background: #c9f1fd;
    cursor: pointer;
  }

  thead, tbody, col{
    border-top: 4px solid white;
    border-left: 4px solid white;
    border-right: 4px solid white;
  }

  #bootstrap-overide thead th{
    line-height: 40px;
    color: white;
  }

  ::-webkit-scrollbar {
    width: .3vw;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 5px grey; 
    border-radius: 10px;
  }
   
  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: white; 
    border-radius: 10px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #6ec4de; 
  }

  .btn-info {
    background: #c9f1fd;
    border-radius: 20px;
    width: 40%;  
    font-family: Comfortaa;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    border: none;
    margin-top: 3vw;
    float: right;
  }

</style>
