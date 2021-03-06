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

    $(".switch-container").on("click", ".feature-checkbox", (e) => {
        const propertyId = e.target.dataset.propertyId;
        const checked = e.target.checked;
        $.ajax({
            url: `${BASE_URL}${propertyId}`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
                "featured": checked
            })
        }).then(() => {
            notification(`Your property has been ${checked ? 'featured' : 'unfeatured'}!`);
        });
    });
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
            function() {
                notification("Thank you! Your message has been sent successfully.");
            },
            function(error) {
                notification("Ooops! Something went wrong, please try again!");
                console.error(error);
            }
        );
    return false; // To block from loading a new page
}

// Set up notifications
function notification(message) {
    var toastHTML = `</span>${message}</span>`;
    M.toast({
        html: toastHTML
    });
}

// Menu items: show active page
/* Orginal code from with modifications for project:
 https://www.infoworld.com/article/3304440/setting-an-active-menu-item-based-on-the-current-url-with-jquery.html */
$(function() {
    setNavigation();
});

function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $("li a").each(function() {
        var href = $(this).attr('href');
        if (path.substring(0, href.length) === href) {
            $(this).closest('li').addClass('active');
        }
    });
}