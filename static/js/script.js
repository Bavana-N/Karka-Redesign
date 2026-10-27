/* =====================================================
   KARKA AI & TECH ACADEMY
   JAVASCRIPT
   ===================================================== */


/* =====================================================
   NAVBAR SCROLL
   ===================================================== */

const header =
    document.querySelector(".site-header");


window.addEventListener("scroll", function () {

    if (!header) return;

    if (window.scrollY > 40) {

        header.classList.add("scrolled");

    } else {

        header.classList.remove("scrolled");

    }

});



/* =====================================================
   MOBILE MENU
   ===================================================== */

const menuBtn =
    document.querySelector(".menu-btn");

const navMenu =
    document.querySelector(".nav-menu");


if (menuBtn && navMenu) {

    menuBtn.addEventListener("click", function () {

        navMenu.classList.toggle("active");

        const isOpen =
            navMenu.classList.contains("active");

        menuBtn.setAttribute(
            "aria-expanded",
            isOpen ? "true" : "false"
        );

    });


    const navLinks =
        navMenu.querySelectorAll("a");


    navLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            navMenu.classList.remove("active");

            menuBtn.setAttribute(
                "aria-expanded",
                "false"
            );

        });

    });

}



/* =========================
   FAQ ACCORDION
========================= */

document.addEventListener("DOMContentLoaded", function () {

    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(function (item) {

        const question = item.querySelector(".faq-question");

        question.addEventListener("click", function () {

            /* Close other FAQ */
            faqItems.forEach(function (otherItem) {

                if (otherItem !== item) {
                    otherItem.classList.remove("active");
                }

            });

            /* Open / Close clicked FAQ */
            item.classList.toggle("active");

        });

    });

});


/* =====================================================
   SMOOTH SCROLL
   ===================================================== */

const internalLinks =
    document.querySelectorAll('a[href^="#"]');


internalLinks.forEach(function (link) {

    link.addEventListener("click", function (event) {

        const targetId =
            this.getAttribute("href");


        if (
            !targetId ||
            targetId === "#"
        ) {

            return;

        }


        const target =
            document.querySelector(targetId);


        if (!target) return;


        event.preventDefault();


        const headerHeight =
            header
                ? header.offsetHeight
                : 0;


        const targetPosition =
            target.getBoundingClientRect().top +
            window.pageYOffset -
            headerHeight -
            10;


        window.scrollTo({

            top: targetPosition,

            behavior: "smooth"

        });

    });

});



/* =====================================================
   SCROLL REVEAL
   ===================================================== */

const revealElements =
    document.querySelectorAll(
        ".feature-card, " +
        ".course-card, " +
        ".project-showcase, " +
        ".benefit-item, " +
        ".timeline-item"
    );


revealElements.forEach(function (element) {

    element.classList.add("reveal");

});


if ("IntersectionObserver" in window) {

    const revealObserver =
        new IntersectionObserver(

            function (entries, observer) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("active");

                        observer.unobserve(
                            entry.target
                        );

                    }

                });

            },

            {
                threshold: 0.12
            }

        );


    revealElements.forEach(function (element) {

        revealObserver.observe(element);

    });

} else {

    revealElements.forEach(function (element) {

        element.classList.add("active");

    });

}



/* =====================================================
   CURRENT YEAR
   ===================================================== */

const yearText =
    document.querySelector(
        ".footer-bottom span"
    );


if (yearText) {

    yearText.textContent =
        "© " +
        new Date().getFullYear() +
        " Karka AI & Tech Academy";

}



/* =====================================================
   PAGE LOADED
   ===================================================== */

console.log(
    "Karka AI & Tech Academy website loaded successfully ✦"
);