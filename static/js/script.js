$(document).ready(function() {
    $('.modal').modal();
    $('.sidenav').sidenav({
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
    $('select').formSelect();
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function() {
            $(this).parent(".select-wrapper").on("change", function() {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function() {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function() {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function() {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

// ..................... Email functionality 
function sendMail(contactForm) {
    emailjs.send("gmail", "SevenTerraces", {
            "from_name": contactForm.name.value,
            "from_telephone": contactForm.telephone.value,
            "from_email": contactForm.email.value,
            "message": contactForm.message.value
        })
        .then(
            function(response) {
                notification("Thank you! Your message has been sent successfully.");
            },
            function(error) {
                notification("Ooops! Something went wrong, please try again!", "danger");
                console.error(error);
            }
        );
    return false; // To block from loading a new page
}
// Set up notifications
function notification(message, alertType = "success") {
    let alert = document.getElementById('alert');
    if (alert) {
        alert.remove();
    }

    let wrapper = document.createElement("div");
    wrapper.setAttribute("id", "alert");
    wrapper.setAttribute("role", "alert");
    wrapper.classList = `alert alert-${alertType} alert-dismissible fade show`;
    wrapper.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
    alert = document.getElementById('alert');
    const bsAlert = new bootstrap.Alert(alert);
    document.body.appendChild(wrapper);
}