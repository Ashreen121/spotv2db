from bs4 import BeautifulSoup

    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>SPOT &#8226; Yaqub, C (Y1)</title>
    <meta charset="utf-8">
    <meta name=viewport content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" type="text/css" href="spot.css">
    <link rel="stylesheet" href="CDNcache/bootstrap.min.css">
    <script src="CDNcache/jquery-3.2.1.slim.min.js"></script>
    <script src="CDNcache/bootstrap.min.js"></script>
    <script src="spot.js"></script>
    </head>
    <body>
    <div class="container"><!-- outer containter for whole page -->
    <table class="cwk">
    
    <tr>
    <td class="boilerplate">SPOT shows marks for COMP courses only. All marks are provisional. <span class="SPOTdeliverableCode">#</span> means an assignment has been submitted but
    not yet marked. An <span class="SPOTdeliverableCode">-S-</span> assignment is summative and counts
    towards your assessment; an <span class="SPOTdeliverableCode">-F-</span> assignment is formative, and marks do
    not count, but you are expected to do every formative assignment.  Any penalties for late submission are applied at the end of the Semester. To request a Late Flag to be
    removed, use
    <!-- removed 201120. <a href="http://studentnet.cs.manchester.ac.uk/student-services/Late_flag.pdf">this form</a>-->
    <!-- addedd 20112 --><a href="https://studentnet.cs.manchester.ac.uk/me/lateflags/" target="_blank"">this form</a> 
    within 1 calendar week of the relevant submission deadline.</td>
    </tr>
    </table>
    <p>&nbsp;</p>
    <ul class="nav nav-tabs">
    <li class="nav-item ">
        <a class="nav-link " href="#sem1" data-toggle="tab">Semester 1</a>
    </li>
    <li class="nav-item active">
        <a class="nav-link active" href="#sem2" data-toggle="tab">Semester 2</a>
    </li>
    </ul><div class="tab-content"> 
    <div class="tab-pane " id="sem1">
    <nav class="navbar d-print-inline fixed-top navbar-expand navbar-light bg-light">

    <div class="collapse navbar-collapse flex-column"  id="navbar">

        <ul class="navbar-nav justify-content-center px-3">
        <li class="nav-item active SPOTdepartment">
            Department of Computer Science &bull; AY2020
        </li>
        </ul>

        <ul class="navbar-nav justify-content-center px-3">
        <li class="nav-item active SPOTstudentName">
        <span style="text-align:center;display:block"> <span class="font-weight:bold">Chaudhry Mohammed Bilal Yaqub</span>
    <br>10805234 &bull; f39003cy &bull; Year 1 &bull; CSwIE</span>
        </li>
        </ul>

        <ul class="navbar-nav justify-content-center w-100 bg-light px-3 d-print ">

    <!- [ year ] dropdown--------------------------------->      
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href=""
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
            year
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">
    <a class="dropdown-item" href="/me/spot/index.php?ay=2020">2020</a>
            </div>
        </li>

    <!- [ courses ] dropdown--------------------------------->      
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href=""
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
            courses
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">
    <a class="dropdown-item" href="#COMP10120">COMP10120</a><a class="dropdown-item" href="#COMP11120">COMP11120</a><a class="dropdown-item" href="#COMP11212">COMP11212</a><a class="dropdown-item" href="#COMP12111">COMP12111</a><a class="dropdown-item" href="#COMP13212">COMP13212</a><a class="dropdown-item" href="#COMP15111">COMP15111</a><a class="dropdown-item" href="#COMP15212">COMP15212</a><a class="dropdown-item" href="#COMP16321">COMP16321</a><a class="dropdown-item" href="#COMP16412">COMP16412</a>
            </div>
        </li>

    <!- [ deadlines ] dropdown--------------------------------->      
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href=""
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
            deadlines
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">



    <a class="dropdown-item"
            href="https://online.manchester.ac.uk/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=calendar-mybb_____calendar-tool" target="_blank">Bb calendar</a>

            <a class="dropdown-item"
            href="https://docs.google.com/spreadsheets/d/11XvSfBHq-kSYZquztFrkjaJJpn6OxDu1uPAkBn-Cie0/edit#gid=794001906" target="_blank">Overview</a>

            </div>
        </li>

    <!- [ help ] dropdown--------------------------------->      
    <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="http://example.com"
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
    help
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">

    <a class="dropdown-item"
            href="https://studentnet.cs.manchester.ac.uk/me" target="_blank">my page</a>

    <a class="dropdown-item"
            href="https://wiki.cs.manchester.ac.uk/index.php/UGHandbook19:Coursework"
            target="_blank" >coursework<br>processes</a>

    <a class="dropdown-item"
            href="http://studentnet.cs.manchester.ac.uk/assessment/mitigatingcircumstances.php?view=ug
            target="_blank" ">mitigating<br>circumstances</a>

    <a class="dropdown-item"
            href="https://studentnet.cs.manchester.ac.uk/me/lateflags/"> Late Flag<br>Removal</a>

    <a class="dropdown-item"
            href="mailto:stewart.blakeway@manchester.ac.uk,toby.howard@manchester.ac.uk?subject=Query%20about%20SPOT">contact</a>
            </div>
        </li>
        </ul>
    </div>
    </nav>
    <div class="container">
    <p>&nbsp</p>
    <a class="anchor" id="COMP10120"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP10120 First Year Team Project (20CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP10120/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:Uli.Sattler@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Uli Sattler</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><tr>
    <td>10120-Quiz1-F-Lab1</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">29</span> /36<br>(81%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>26-Nov-20 10:07</td>
    
    </tr><tr>
    <td>10120-Quiz2-F-Lab 2</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">34</span> /41<br>(83%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>26-Nov-20 14:01</td>
    
    </tr><tr>
    <td>10120-Quiz3-F-Lab 3</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">42</span> /50<br>(84%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>08-Dec-20 20:17</td>
    
    </tr><tr>
    <td>10120-Quiz4-F-Lab 4</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">46</span> /60<br>(77%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>09-Dec-20 23:32</td>
    
    </tr><tr>
    <td>10120-Quiz5-F-Lab 5</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">80</span> /200<br>(40%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>18-Dec-20 13:47</td>
    
    </tr><tr>
    <td>10120-Quiz5-F-Lab 6</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">8</span> /14<br>(57%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>18-Dec-20 13:49</td>
    
    </tr><tr>
    <td>10120-Quiz7-F-Lab 7</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">14</span> /21<br>(67%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>17-Dec-20 21:24</td>
    
    </tr><tr>
    <td>10120-Quiz8-F-Lab 8</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">8</span> /10<br>(80%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>09-Dec-20 23:40</td>
    
    </tr><tr>
    <td>10120-presentation1-S-Sem 1 Presentation</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">13</span> /16<br>(81%)
    </td>
    <td>18-Dec-20 18:00</td>
    <td>18-Dec-20 10:28</td>
    
    </tr><tr>
    <td>10120-LabEngagement-S-LabEngagement</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">#</span> /100<br>
    </td>
    <td>13-Jan-21 18:00</td>
    <td></td>
    
    </tr><tr>
    <td>10120-QuizEngagement-S-QuizEngagement</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">#</span> /100<br>
    </td>
    <td>13-Jan-21 18:00</td>
    <td></td>
    
    </tr><tr>
    <td>10120-cv-F-CV</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">2</span> /2<br>(100%)
    </td>
    <td>08-Feb-21 09:00</td>
    <td>08-Feb-21 08:10</td>
    
    </tr><tr>
    <td>10120-report-S-Reflective Report</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">7</span> /8<br>(88%)
    </td>
    <td>08-Feb-21 09:00</td>
    <td>08-Feb-21 08:05</td>
    
    </tr><td>10120-project-F-Project Code</td><td></td><td>16-Apr-21 17:00</td><td></td></tr><td>10120-presentation2-S-Presentation</td><td></td><td>30-Apr-21 17:00</td><td></td></tr><td>10120-report2-S-Final Report</td><td></td><td>14-May-21 16:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP10120: <b>33%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP11120"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP11120 Mathematical Techniques for Computer Science (20CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP11120/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:andrea.schalk@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Andrea Schalk</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><tr>
    <td>Exam total</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">47</span> /60<br>(78%)
    </td>
    <td>not applicable</td>
    <td>16-Jan-21 08:45</td>
    
    </tr><tr>
    <td>11120-sheet00-F-Sheet 0</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">3</span> /5<br>(60%)
    </td>
    <td>05-Oct-20 11:00</td>
    <td>05-Oct-20 08:21</td>
    
    </tr><tr>
    <td>11120-sheet01-S-Sheet 1</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>12-Oct-20 11:00</td>
    <td>12-Oct-20 10:35</td>
    
    </tr><tr>
    <td>11120-sheet02-S-Sheet 2</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">5</span> /5<br>(100%)
    </td>
    <td>19-Oct-20 11:00</td>
    <td>19-Oct-20 10:25</td>
    
    </tr><tr>
    <td>11120-sheet03-S-Sheet 3</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">5</span> /5<br>(100%)
    </td>
    <td>26-Oct-20 12:00</td>
    <td>26-Oct-20 11:09</td>
    
    </tr><tr>
    <td>11120-sheet04-S-Sheet 4</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>02-Nov-20 12:00</td>
    <td>02-Nov-20 10:39</td>
    
    </tr><tr>
    <td>11120-sheet05-S-Sheet 5</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>09-Nov-20 12:00</td>
    <td>09-Nov-20 10:00</td>
    
    </tr><tr>
    <td>11120-sheet06-S-Sheet 6</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>16-Nov-20 12:00</td>
    <td>16-Nov-20 11:55</td>
    
    </tr><tr>
    <td>11120-sheet07-S-Sheet 7</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>23-Nov-20 12:00</td>
    <td>23-Nov-20 11:15</td>
    
    </tr><tr>
    <td>11120-sheet08-S-Sheet 8</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">5</span> /5<br>(100%)
    </td>
    <td>30-Nov-20 12:00</td>
    <td>30-Nov-20 11:50</td>
    
    </tr><td>11120-sheet09-S-Sheet 9</td><td></td><td>07-Dec-20 12:00</td><td></td></tr><td>11120-sheet10-S-Sheet 10</td><td></td><td>14-Dec-20 12:00</td><td></td></tr><tr>
    <td>11120-sheet11-S-Sheet 11</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">1</span> /5<br>(20%)
    </td>
    <td>15-Feb-21 12:00</td>
    <td>15-Feb-21 11:59</td>
    
    </tr><tr>
    <td>11120-sheet12-S-Sheet 12</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">2</span> /5<br>(40%)
    </td>
    <td>22-Feb-21 12:00</td>
    <td>22-Feb-21 11:00</td>
    
    </tr><tr>
    <td>11120-sheet13-S-Sheet 13</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>01-Mar-21 12:00</td>
    <td>01-Mar-21 10:41</td>
    
    </tr><tr>
    <td>11120-sheet14-S-Sheet 14</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>08-Mar-21 12:00</td>
    <td>08-Mar-21 11:12</td>
    
    </tr><tr>
    <td>11120-sheet15-S-Sheet 15</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>15-Mar-21 12:00</td>
    <td>15-Mar-21 11:58</td>
    
    </tr><tr>
    <td>11120-sheet16-S-Sheet 16</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>22-Mar-21 12:00</td>
    <td>22-Mar-21 11:28</td>
    
    </tr><tr>
    <td>11120-sheet17-S-Sheet 17</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">#</span> /5<br>
    </td>
    <td>12-Apr-21 11:00</td>
    <td></td>
    
    </tr><td>11120-sheet18-S-Sheet 18</td><td></td><td>19-Apr-21 11:00</td><td></td></tr><td>11120-sheet19-S-Sheet 19</td><td></td><td>26-Apr-21 11:00</td><td></td></tr><td>11120-sheet20-S-Sheet 20</td><td></td><td>03-May-21 11:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP11120: <b>50%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP12111"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP12111 Fundamentals of Computer Engineering (10CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP12111/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:P.Nutter@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Paul Nutter</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><tr>
    <td>12111-Lab1-F-Adders</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">97</span> /100<br>(97%)
    </td>
    <td>23-Oct-20 17:00</td>
    <td>29-Oct-20 17:42</td>
    
    </tr><tr>
    <td>12111-Lab2-S-Combinatorial</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">100</span> /100<br>(100%)
    </td>
    <td>06-Nov-20 18:00</td>
    <td>18-Nov-20 11:16</td>
    
    </tr><tr>
    <td>12111-Test-S-Midterm test</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">13</span> /14<br>(93%)
    </td>
    <td>13-Nov-20 18:00</td>
    <td>13-Nov-20 17:22</td>
    
    </tr><tr>
    <td>12111-Lab3-S-Sequential</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">95</span> /100<br>(95%)
    </td>
    <td>04-Dec-20 18:00</td>
    <td>18-Dec-20 13:05</td>
    
    </tr><tr>
    <td>12111-Lab4-S-The Processor</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">94</span> /100<br>(94%)
    </td>
    <td>18-Dec-20 18:00</td>
    <td>15-Jan-21 11:44</td>
    
    </tr><tr>
    <td>COMP12111 Exam 2020-21</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">46.5</span> /60<br>(78%)
    </td>
    <td>25-Jan-21 16:00</td>
    <td>25-Jan-21 14:46</td>
    
    </tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP12111: <b>96%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP15111"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP15111 Fundamentals of Computer Architecture (10CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP15111/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:Christos.Kotselidis@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Christos Kotselidis</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><tr>
    <td>15111-LAB1-S-Introduction</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">10</span> /10<br>(100%)
    </td>
    <td>25-Oct-20 23:59</td>
    <td>02-Mar-21 23:37</td>
    
    </tr><tr>
    <td>15111-LAB2-S-Control Structures</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">10</span> /10<br>(100%)
    </td>
    <td>08-Nov-20 23:59</td>
    <td>02-Mar-21 23:38</td>
    
    </tr><tr>
    <td>15111-LAB3-S-Addressing</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">10</span> /10<br>(100%)
    </td>
    <td>22-Nov-20 23:59</td>
    <td>02-Mar-21 23:39</td>
    
    </tr><tr>
    <td>15111-LAB4-S-Methods</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">9</span> /10<br>(90%)
    </td>
    <td>06-Dec-20 23:59</td>
    <td>02-Mar-21 23:40</td>
    
    </tr><tr>
    <td>COMP15111 Exam 2020-2021</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">45</span> /50<br>(90%)
    </td>
    <td>27-Jan-21 16:00</td>
    <td>27-Jan-21 14:11</td>
    
    </tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP15111: <b>98%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP16321"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP16321  Introduction to Programming 1 (20CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP16321/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:gareth.henshall@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Gareth Henshall</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><tr>
    <td>16321-LAB1-F-QUIZ</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">12</span> /60<br>(20%)
    </td>
    <td>not applicable</td>
    <td>09-Nov-20 15:37</td>
    
    </tr><tr>
    <td>16321-LAB2-F-QUIZ</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">47</span> /60<br>(78%)
    </td>
    <td>not applicable</td>
    <td>11-Nov-20 02:13</td>
    
    </tr><tr>
    <td>16321-LAB3-F-QUIZ</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">46</span> /60<br>(77%)
    </td>
    <td>not applicable</td>
    <td>11-Nov-20 01:15</td>
    
    </tr><tr>
    <td>16321-LAB4-F-QUIZ</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">49</span> /60<br>(82%)
    </td>
    <td>not applicable</td>
    <td>10-Nov-20 22:50</td>
    
    </tr><tr>
    <td>16321-LAB5-F-QUIZ</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">50</span> /60<br>(83%)
    </td>
    <td>not applicable</td>
    <td>18-Jan-21 13:03</td>
    
    </tr><td>16321-LAB6-F-QUIZ</td><td></td><td>not applicable</td><td></td></tr><td>16321-LAB7-F-QUIZ</td><td></td><td>not applicable</td><td></td></tr><tr>
    <td>16321-LAB8-F-QUIZ</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">42</span> /60<br>(70%)
    </td>
    <td>not applicable</td>
    <td>17-Jan-21 10:53</td>
    
    </tr><tr>
    <td>16321-Cwk1-S-Python Basics</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">98.7</span> /100<br>(99%)
    </td>
    <td>06-Nov-20 18:00</td>
    <td>06-Nov-20 17:47</td>
    
    </tr><tr>
    <td>16321-Test1-S-Midterm 01</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">28.4</span> /30<br>(95%)
    </td>
    <td>11-Nov-20 18:00</td>
    <td>11-Nov-20 13:12</td>
    
    </tr><tr>
    <td>16321-Cwk2-S-Advanced Python</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">89.3</span> /100<br>(89%)
    </td>
    <td>04-Dec-20 18:00</td>
    <td>11-Dec-20 16:54</td>
    
    </tr><tr>
    <td>16321-Test2-S-Midterm 02</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">29</span> /30<br>(97%)
    </td>
    <td>15-Dec-20 18:00</td>
    <td>15-Dec-20 15:28</td>
    
    </tr><tr>
    <td>COMP16321 Exam 2020-21</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">56</span> /60<br>(93%)
    </td>
    <td>20-Jan-21 16:00</td>
    <td>20-Jan-21 14:21</td>
    
    </tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP16321: <b>94%</b></td>
    </tr></table>
    <p class="SPOTstatus"><br>Assessments via Benchmark or Gitmark appear in SPOT immediately; Blackboard assessments update once a day, last update: 13-Apr-21 11:38</p>
    </div><!-- container -->
    </div> <!-- sem1 -->
    <div class= "tab-pane active" id="sem2">
    <nav class="navbar d-print-inline fixed-top navbar-expand navbar-light bg-light">

    <div class="collapse navbar-collapse flex-column"  id="navbar">

        <ul class="navbar-nav justify-content-center px-3">
        <li class="nav-item active SPOTdepartment">
            Department of Computer Science &bull; AY2020
        </li>
        </ul>

        <ul class="navbar-nav justify-content-center px-3">
        <li class="nav-item active SPOTstudentName">
        <span style="text-align:center;display:block"> <span class="font-weight:bold">Chaudhry Mohammed Bilal Yaqub</span>
    <br>10805234 &bull; f39003cy &bull; Year 1 &bull; CSwIE</span>
        </li>
        </ul>

        <ul class="navbar-nav justify-content-center w-100 bg-light px-3 d-print ">

    <!- [ year ] dropdown--------------------------------->      
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href=""
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
            year
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">
    <a class="dropdown-item" href="/me/spot/index.php?ay=2020">2020</a>
            </div>
        </li>

    <!- [ courses ] dropdown--------------------------------->      
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href=""
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
            courses
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">
    <a class="dropdown-item" href="#COMP10120">COMP10120</a><a class="dropdown-item" href="#COMP11120">COMP11120</a><a class="dropdown-item" href="#COMP11212">COMP11212</a><a class="dropdown-item" href="#COMP12111">COMP12111</a><a class="dropdown-item" href="#COMP13212">COMP13212</a><a class="dropdown-item" href="#COMP15111">COMP15111</a><a class="dropdown-item" href="#COMP15212">COMP15212</a><a class="dropdown-item" href="#COMP16321">COMP16321</a><a class="dropdown-item" href="#COMP16412">COMP16412</a>
            </div>
        </li>

    <!- [ deadlines ] dropdown--------------------------------->      
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href=""
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
            deadlines
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">



    <a class="dropdown-item"
            href="https://online.manchester.ac.uk/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=calendar-mybb_____calendar-tool" target="_blank">Bb calendar</a>

            <a class="dropdown-item"
            href="https://docs.google.com/spreadsheets/d/11XvSfBHq-kSYZquztFrkjaJJpn6OxDu1uPAkBn-Cie0/edit#gid=794001906" target="_blank">Overview</a>

            </div>
        </li>

    <!- [ help ] dropdown--------------------------------->      
    <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="http://example.com"
        id="navbarDropdownMenuLink" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
    help
            </a>
            <div class="dropdown-menu"
        aria-labelledby="navbarDropdownMenuLink">

    <a class="dropdown-item"
            href="https://studentnet.cs.manchester.ac.uk/me" target="_blank">my page</a>

    <a class="dropdown-item"
            href="https://wiki.cs.manchester.ac.uk/index.php/UGHandbook19:Coursework"
            target="_blank" >coursework<br>processes</a>

    <a class="dropdown-item"
            href="http://studentnet.cs.manchester.ac.uk/assessment/mitigatingcircumstances.php?view=ug
            target="_blank" ">mitigating<br>circumstances</a>

    <a class="dropdown-item"
            href="https://studentnet.cs.manchester.ac.uk/me/lateflags/"> Late Flag<br>Removal</a>

    <a class="dropdown-item"
            href="mailto:stewart.blakeway@manchester.ac.uk,toby.howard@manchester.ac.uk?subject=Query%20about%20SPOT">contact</a>
            </div>
        </li>
        </ul>
    </div>
    </nav>
    <div class="container">
    <p>&nbsp</p>
    <a class="anchor" id="COMP10120"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP10120 First Year Team Project (20CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP10120/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:Uli.Sattler@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Uli Sattler</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><tr>
    <td>10120-Quiz1-F-Lab1</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">29</span> /36<br>(81%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>26-Nov-20 10:07</td>
    
    </tr><tr>
    <td>10120-Quiz2-F-Lab 2</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">34</span> /41<br>(83%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>26-Nov-20 14:01</td>
    
    </tr><tr>
    <td>10120-Quiz3-F-Lab 3</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">42</span> /50<br>(84%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>08-Dec-20 20:17</td>
    
    </tr><tr>
    <td>10120-Quiz4-F-Lab 4</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">46</span> /60<br>(77%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>09-Dec-20 23:32</td>
    
    </tr><tr>
    <td>10120-Quiz5-F-Lab 5</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">80</span> /200<br>(40%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>18-Dec-20 13:47</td>
    
    </tr><tr>
    <td>10120-Quiz5-F-Lab 6</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">8</span> /14<br>(57%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>18-Dec-20 13:49</td>
    
    </tr><tr>
    <td>10120-Quiz7-F-Lab 7</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">14</span> /21<br>(67%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>17-Dec-20 21:24</td>
    
    </tr><tr>
    <td>10120-Quiz8-F-Lab 8</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">8</span> /10<br>(80%)
    </td>
    <td>18-Dec-20 17:00</td>
    <td>09-Dec-20 23:40</td>
    
    </tr><tr>
    <td>10120-presentation1-S-Sem 1 Presentation</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">13</span> /16<br>(81%)
    </td>
    <td>18-Dec-20 18:00</td>
    <td>18-Dec-20 10:28</td>
    
    </tr><tr>
    <td>10120-LabEngagement-S-LabEngagement</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">#</span> /100<br>
    </td>
    <td>13-Jan-21 18:00</td>
    <td></td>
    
    </tr><tr>
    <td>10120-QuizEngagement-S-QuizEngagement</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">#</span> /100<br>
    </td>
    <td>13-Jan-21 18:00</td>
    <td></td>
    
    </tr><tr>
    <td>10120-cv-F-CV</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">2</span> /2<br>(100%)
    </td>
    <td>08-Feb-21 09:00</td>
    <td>08-Feb-21 08:10</td>
    
    </tr><tr>
    <td>10120-report-S-Reflective Report</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">7</span> /8<br>(88%)
    </td>
    <td>08-Feb-21 09:00</td>
    <td>08-Feb-21 08:05</td>
    
    </tr><td>10120-project-F-Project Code</td><td></td><td>16-Apr-21 17:00</td><td></td></tr><td>10120-presentation2-S-Presentation</td><td></td><td>30-Apr-21 17:00</td><td></td></tr><td>10120-report2-S-Final Report</td><td></td><td>14-May-21 16:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP10120: <b>33%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP11120"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP11120 Mathematical Techniques for Computer Science (20CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP11120/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:andrea.schalk@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Andrea Schalk</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><tr>
    <td>Exam total</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">47</span> /60<br>(78%)
    </td>
    <td>not applicable</td>
    <td>16-Jan-21 08:45</td>
    
    </tr><tr>
    <td>11120-sheet00-F-Sheet 0</td>
    <td class="table-notlateFlag">
                <span class="formativeMark">3</span> /5<br>(60%)
    </td>
    <td>05-Oct-20 11:00</td>
    <td>05-Oct-20 08:21</td>
    
    </tr><tr>
    <td>11120-sheet01-S-Sheet 1</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>12-Oct-20 11:00</td>
    <td>12-Oct-20 10:35</td>
    
    </tr><tr>
    <td>11120-sheet02-S-Sheet 2</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">5</span> /5<br>(100%)
    </td>
    <td>19-Oct-20 11:00</td>
    <td>19-Oct-20 10:25</td>
    
    </tr><tr>
    <td>11120-sheet03-S-Sheet 3</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">5</span> /5<br>(100%)
    </td>
    <td>26-Oct-20 12:00</td>
    <td>26-Oct-20 11:09</td>
    
    </tr><tr>
    <td>11120-sheet04-S-Sheet 4</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>02-Nov-20 12:00</td>
    <td>02-Nov-20 10:39</td>
    
    </tr><tr>
    <td>11120-sheet05-S-Sheet 5</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>09-Nov-20 12:00</td>
    <td>09-Nov-20 10:00</td>
    
    </tr><tr>
    <td>11120-sheet06-S-Sheet 6</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>16-Nov-20 12:00</td>
    <td>16-Nov-20 11:55</td>
    
    </tr><tr>
    <td>11120-sheet07-S-Sheet 7</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">3</span> /5<br>(60%)
    </td>
    <td>23-Nov-20 12:00</td>
    <td>23-Nov-20 11:15</td>
    
    </tr><tr>
    <td>11120-sheet08-S-Sheet 8</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">5</span> /5<br>(100%)
    </td>
    <td>30-Nov-20 12:00</td>
    <td>30-Nov-20 11:50</td>
    
    </tr><td>11120-sheet09-S-Sheet 9</td><td></td><td>07-Dec-20 12:00</td><td></td></tr><td>11120-sheet10-S-Sheet 10</td><td></td><td>14-Dec-20 12:00</td><td></td></tr><tr>
    <td>11120-sheet11-S-Sheet 11</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">1</span> /5<br>(20%)
    </td>
    <td>15-Feb-21 12:00</td>
    <td>15-Feb-21 11:59</td>
    
    </tr><tr>
    <td>11120-sheet12-S-Sheet 12</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">2</span> /5<br>(40%)
    </td>
    <td>22-Feb-21 12:00</td>
    <td>22-Feb-21 11:00</td>
    
    </tr><tr>
    <td>11120-sheet13-S-Sheet 13</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>01-Mar-21 12:00</td>
    <td>01-Mar-21 10:41</td>
    
    </tr><tr>
    <td>11120-sheet14-S-Sheet 14</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>08-Mar-21 12:00</td>
    <td>08-Mar-21 11:12</td>
    
    </tr><tr>
    <td>11120-sheet15-S-Sheet 15</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>15-Mar-21 12:00</td>
    <td>15-Mar-21 11:58</td>
    
    </tr><tr>
    <td>11120-sheet16-S-Sheet 16</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">4</span> /5<br>(80%)
    </td>
    <td>22-Mar-21 12:00</td>
    <td>22-Mar-21 11:28</td>
    
    </tr><tr>
    <td>11120-sheet17-S-Sheet 17</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">#</span> /5<br>
    </td>
    <td>12-Apr-21 11:00</td>
    <td></td>
    
    </tr><td>11120-sheet18-S-Sheet 18</td><td></td><td>19-Apr-21 11:00</td><td></td></tr><td>11120-sheet19-S-Sheet 19</td><td></td><td>26-Apr-21 11:00</td><td></td></tr><td>11120-sheet20-S-Sheet 20</td><td></td><td>03-May-21 11:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP11120: <b>50%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP11212"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP11212 Fundamentals of Computation (10CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP11212/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:sean.k.bechhofer@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Sean Bechhofer</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><td>11212-sheet1-F-Sheet 1</td><td></td><td>07-Feb-20 18:00</td><td></td></tr><td>11212-sheet2-F-Sheet 2</td><td></td><td>14-Feb-20 18:00</td><td></td></tr><td>11212-sheet3-F-Sheet 3</td><td></td><td>21-Feb-20 18:00</td><td></td></tr><td>11212-sheet4-F-Sheet 4</td><td></td><td>28-Feb-20 18:00</td><td></td></tr><td>11212-sheet5-F-Sheet 5</td><td></td><td>06-Mar-20 18:00</td><td></td></tr><td>11212-sheet6-F-Sheet 6</td><td></td><td>13-Mar-20 18:00</td><td></td></tr><td>11212-sheet7-F-Sheet 7</td><td></td><td>20-Mar-20 18:00</td><td></td></tr><td>11212-sheet8-F-Sheet 8</td><td></td><td>27-Mar-20 18:00</td><td></td></tr><td>11212-sheet9-F-Sheet 9</td><td></td><td>24-Apr-20 17:00</td><td></td></tr><td>11212-sheet10-F-Sheet 10</td><td></td><td>01-May-20 17:00</td><td></td></tr><tr>
    <td>11212-exercise1-S-Exercise 1</td>
    <td class="table-notlateFlag">
                <span class="summativeMark">7</span> /8<br>(88%)
    </td>
    <td>26-Feb-21 18:00</td>
    <td>26-Feb-21 12:39</td>
    
    </tr><tr>
    <td>11212-exercise2-S-Exercise 2</td>
    <td class="table-lateFlag">
                <span class="summativeMark">#</span> /8<br> LATE
    </td>
    <td>19-Mar-21 18:00</td>
    <td></td>
    
    </tr><td>11212-exercise3-S-Exercise 3</td><td></td><td>23-Apr-21 17:00</td><td></td></tr><td>11212-exercise4-S-Exercise 4</td><td></td><td>07-May-21 17:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP11212: <b>22%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP13212"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP13212 Data Science (10CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP13212/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:jonathan.l.shapiro@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Jon Shapiro</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><td>13212-LAB4-S-Statistical reasoning</td><td></td><td>16-Apr-21 12:27</td><td></td></tr><td>13212-LAB5-S-Machine Learning</td><td></td><td>07-May-21 17:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP13212: <b>0%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP15212"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP15212 Operating Systems (10CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP15212/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:steve.pettifer@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Steve Pettifer</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><td>15212-Lab3-S-Cache</td><td></td><td>16-Apr-21 17:00</td><td></td></tr><td>15212-Lab5-S-Experiment</td><td></td><td>14-May-21 17:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP15212: <b>0%</b></td>
    </tr></table><p>&nbsp</p>
    <a class="anchor" id="COMP16412"></a>
    <table class="cwk">
    <tr>
    <td class="courseHeader" colspan="4"><b>COMP16412 Programming 2 (10CR)</b>	
    <br><a href="http://studentnet.cs.manchester.ac.uk/ugt/2020/COMP16412/syllabus" target="_blank" class="btn btn-primary d-print-none" role="button">syllabus</a>
    <a href="mailto:markel.vigo@manchester.ac.uk" class="btn btn-primary d-print-none" role="button">email leader Markel Vigo</a></p>
    </td>
    </tr>

    <tr>
    <th style="width:50%">Assignment</th>
    <th style="width:10%">Mark /max</th>
    <th style="width:20%">Deadline</th>
    <th style="width:20%">Date marked</th>
    
    </tr><td>16412-Cwk1-S-Part-1</td><td></td><td>12-Mar-21 18:00</td><td></td></tr><td>16412-Cwk2-S-Part-2</td><td></td><td>30-Apr-21 17:00</td><td></td></tr><tr>
    <td colspan="4" class="totalSoFar">Weighted summative coursework average for COMP16412: <b>0%</b></td>
    </tr></table>
    <p class="SPOTstatus"><br>Assessments via Benchmark or Gitmark appear in SPOT immediately; Blackboard assessments update once a day, last update: 13-Apr-21 11:38</p>
    </div><!-- container -->
    </div><!-- tab-content --></div><!-- outer containter for whole page -->
    </body>
    </html>
    '''
    
    parsed = BeautifulSoup(html, "html.parser")
    anchorPosition = parsed.select(".table-notlateFlag")
    anchorPositionTutors = parsed.select(".courseHeader")
    anchorPositionName = parsed.select(".font-weight\:bold")
    
    studentName = anchorPositionName[1].get_text()
    
    with open("spotV2.csv", "w") as database:
    csv_writer = writer(database)
    csv_writer.writerow(
        ["Course", "Assignment", "Marks", "Deadline", "Student Name"])
    
    with open("tutorsPage.csv", "w") as database:
    csv_writer = writer(database)
    csv_writer.writerow(
        ["Course", "Credits", "Students", "Courseleader", "Email", "Assessment Method"])
    
    courseLinks = []
    courses = []
    for i in anchorPositionTutors:
        link = ((i.find('a'))['href'])
        courseLinks.append(link)
