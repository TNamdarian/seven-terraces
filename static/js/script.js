 $(document).ready(function() {
     $(".sidenav").sidenav({
         edge: "right"
     });
     $('.datepicker').datepicker({
         format: "dd mmmm, yyyy",
         yearRange: 3,
         showClearBtn: true,
         i18n: {
             done: "Select"
         }
     });
 });
 
// The original code was written by Tim Nelson at Code Institute: https://github.com/Code-Institute-Solutions/flask-sqlalchemy-task-manager/blob/main/12_deploying_our_project_to_heroku/taskmanager/static/js/script.js
 document.addEventListener("DOMContentLoaded", function() {
     // select initialization
     let selects = document.querySelectorAll("select");
     M.FormSelect.init(selects);
 });