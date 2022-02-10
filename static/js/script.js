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

 document.addEventListener("DOMContentLoaded", function() {
     // select initialization
     let selects = document.querySelectorAll("select");
     M.FormSelect.init(selects);
 });