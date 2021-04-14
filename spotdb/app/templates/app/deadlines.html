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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <title>SPOTv2</title>
  </head>
  <!-- Arbitrary id to give it more priority to overide some Bootstrap stylings -->
  <body id="bootstrap-overide">
    <div>
      {% scrape_now 'https://studentnet.cs.manchester.ac.uk/me/spot/' as success_message %}
      <strong> {{ success_message }} </strong>
    </div>
    <div class="row">
      <div class="col-sm-3">
        <section class="timeline">
          <ul id = 'ul'>
            
            <!-- more list items here -->

          </ul>
            <script type="text/javascript">
               var today = new Date();
               var courseInfos = [{duedate: "2021/04/02 18:00",coursename: "COMPxxx",cwkname:"cousework1"}, 
                                 {duedate: "2021/04/07 18:00",coursename: "COMPxxx",cwkname:"cousework2"}, 
                                 {duedate: "2021/04/11 19:00",coursename: "COMPxxx",cwkname:"cousework3"}, 
                                 {duedate: "2021/04/09 18:00",coursename: "COMPxxx",cwkname:"cousework4"}];
               var courseInfos = courseInfos.sort ((a,b) => new Date(a.duedate).getTime() - new Date(b.duedate).getTime());
              
               for (i=0; i<courseInfos.length; i++) {
                 var number = i.toString();

                 ul = document.getElementById('ul');
                 
                 var newLi = document.createElement('li');
                 var newLi = document.getElementById("ul").appendChild(newLi);
                 var newLi = newLi.setAttribute("id", "li"+number);
                 var newDiv = document.createElement('div');
                 var newDiv = document.getElementById("li"+number).appendChild(newDiv);
                 var newDiv = newDiv.setAttribute("id", "div"+number);
                 var  newTime = document.createElement('time');
                 var  newTime = document.getElementById("div"+number).appendChild(newTime);
                 var newP = document.createElement('p');
                 var newP = document.getElementById("div"+number).appendChild(newP);
                 var newSignal = document.createElement('signal');
                 var newSignal = document.getElementById("div"+number).appendChild(newSignal);
                 var newSignal = newSignal.setAttribute("id", "signal"+number);
                 
                 newTime.innerHTML = courseInfos[i].duedate;
                 newP.innerHTML = courseInfos[i].coursename + " "+courseInfos[i].cwkname;
                 
                 var message ="";
                 var d1 = courseInfos[i].duedate;
                 var due = new Date(d1);
                 var datediff = due.getTime()- today.getTime();
                 var daydiff =Math.floor(datediff / (24 * 3600 * 1000));
                 if (daydiff<=7) {
                     message = "due soon";
                 }
                 document.getElementById("signal"+number).innerHTML = message;
               }

              //detect how long till due date  

             </script>

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
          <table class = "table", style="margin-bottom: 0;">
            <colgroup>
              <col class="course" span="1">
              <col class="course-info" span="2">
            </colgroup>
            <thead>
              <tr id="table-head">
                <th id="cell-topleft" scope="col", style="width: 33%;">Courses</th>
                <th scope="col", style="width: 33%;" >Assignments</th>
                <th id="cell-topright" scope="col", style="width: 33.5%;">Due Dates</th>
              </tr>
            </thead>
          </table>
          <div class="tablelocker ", id = "packageThing">
            <table id="table" class="table table-borderless" style="margin: 0;">
              <colgroup>
                <col class="course" span="1">
                <col class="course-info" span="2">
              </colgroup>
              
            </table>
          </div>
          
        </div>
        <style>.addToCalendar {background-color:#44c767;border-radius:28px;border:1px solid #18ab29;display:inline-block;cursor:pointer;color:#ffffff;font-family:Arial;font-size:16px;padding:16px 31px;text-decoration:none;text-shadow:0px 1px 0px #2f6627;}.addToCalendar:hover {background-color:#5cbf2a;}.addToCalendar:active {position:relative;top:1px;}
        </style>
        <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&dates=20210413T211500Z%2F20210413T214500Z" class="btn btn-info">Add to Calendar</a>
      </div>
    </div>
    
      <script type="text/javascript">
        var crs = ["COMP10120", "COMP11120", "COMP12111", "COMP15111", "COMP16321", "COMP11212", "COMP13212", "COMP15212", "COMP16421"];
        var crswrk = ["Assignment 1", "Assignment 2", "Assignment 3", "Assignment 4", "Assignment 5",
                      "Assignment 6", "Assignment 7", "Assignment 8", "Assignment 9", "Assignment 10",
                      "Assignment 11", "Assignment 12"];
        var crswrk_date = ["01/01/2021", "02/01/2021", "03/01/2021", "04/01/2021", "05/01/2021",
                           "06/01/2021", "07/01/2021", "08/01/2021", "09/01/2021", "10/01/2021",
                           "11/01/2021", "12/01/2021"];

        for (var i = 0; i < crs.length; i++) {
          var crs_row = document.createElement("tbody");
          crs_row.setAttribute("id", "course[" + i + "]");
          crs_row.setAttribute("onclick", "toggleInfo(" + i + ")");
          crs_row.setAttribute("onmouseover", "mouseOver(" + i + ")");
          crs_row.setAttribute("onmouseleave", "mouseLeave(" + i + ")");


          for (var j = 0; j < crswrk.length; j++) {
            var crswrk_row = document.createElement("tr");

            // For the Courses coloumn
            if (j == 0) {
              var crs_th = document.createElement("th");
              crs_th.setAttribute("scope", "row");
              crs_th.setAttribute("rowspan", crswrk.length);
              crs_th.setAttribute("style", "width: 33%;");
              crs_th.innerHTML = crs[i];
              crswrk_row.appendChild(crs_th);
            }

            var crswrk_cell = document.createElement("td");
            var crswrk_date_cell = document.createElement("td");
            crswrk_cell.innerHTML = crswrk[j];
            crswrk_date_cell.innerHTML = crswrk_date[j];
            crswrk_cell.setAttribute("style", "width: 33%;");
            crswrk_date_cell.setAttribute("style", "width: 33%;");

            crswrk_row.appendChild(crswrk_cell);
            crswrk_row.appendChild(crswrk_date_cell);
            crs_row.appendChild(crswrk_row);
          }
          document.getElementById("table").appendChild(crs_row);
          for (k = 3; k < crswrk.length; k++) {
            crs_row.querySelectorAll("tr")[k].style.display = "none";
          }
        }

        var click_turn = 0;
        function toggleInfo(crs_index) {
          crs_row_clicked = document.getElementById("course[" + crs_index + "]");
          if (click_turn % 2 == 0) {

            // Hides the entire table
            for (x = 0; x < crs.length; x++) {
              document.getElementById("course[" + x + "]").style.display = "none";
            }
            // Unhides the clicked course
            crs_row_clicked.style.display = "table-row-group";
            // Unhides all the assignments for the clicked course
            for (k = 0; k < crswrk.length; k++) {
              crs_row_clicked.querySelectorAll("tr")[k].style.display = "table-row";
            }

          }

          else if (click_turn % 2 == 1) {

            // Hides the assignments
            for (y = 3; y < crswrk.length; y++) {
              crs_row_clicked.querySelectorAll("tr")[y].style.display = "none";
            }
            // Unhides the other courses
            for (z = 0; z < crs.length; z++) {
              document.getElementById("course[" + z + "]").style.display = "table-row-group";
            }

          }
          click_turn++;
        }

        function mouseOver(crs_index) {
          var tbody = document.getElementById("course[" + crs_index + "]");
          tbody.style.backgroundColor = "#edfaff";
        }

        function mouseLeave(crs_index) {
          var tbody = document.getElementById("course[" + crs_index + "]");
          tbody.style.backgroundColor = "#c9f1fd";
        }

      </script>

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
    height: 100vh;
    margin: 0;
    overflow-y: hidden;
  }
  .col {
    height: 100vh;
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
  }

  .timeline {
    font: normal 16px/1.5 "Helvetica Neue", sans-serif;
    background: #FFFFFF;
    color: #fff;
    overflow-x: hidden;
    padding-bottom: 50px;
    
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

/*html {
  background: linear-gradient(to left, #1976D2 0%, #6ec4de 100%);
  height: 100%;
}*/
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
  width: 25%;  
  font-family: Comfortaa;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  border: none;
  margin-top: 3vw;
  float: right;
}

</style>
