!function () {
    function e(e) {
        e = e || window.event, e.preventDefault && e.preventDefault(), e.returnValue = !1
    }

    function n(n) {
        for (var o = w.length; o--;) if (n.keyCode === w[o]) return void e(n)
    }

    function o(n) {
        e(n)
    }

    function t(e) {
    }

    function i() {
        window.onmousewheel = document.onmousewheel = t, document.onkeydown = n, document.body.ontouchmove = o
    }

    function l() {
        window.onmousewheel = document.onmousewheel = document.onkeydown = document.body.ontouchmove = null
    }

    function s() {
        return window.pageYOffset || p.scrollTop
    }

    function r() {
        if (a = s(), u && !f) {
            if (0 > a) return !1;
            window.scrollTo(0, 0)
        }
        return classie.has(v, "notrans") ? (classie.remove(v, "notrans"), !1) : m ? !1 : void (0 >= a && c ? d(0) : a > 0 && !c && d(1))
    }

    function d(e) {
        m = !0, e ? classie.add(v, "modify") : (u = !0, i(), classie.remove(v, "modify")), setTimeout(function () {
            c = !c, m = !1, e && (u = !1, l())
        }, 600)
    }

    $(window).load(function () {
        $("#preloader").delay(1e3).fadeOut("slow")
    });
    var a, c, u, m, f = function () {
            var e, n = -1, o = window.navigator.userAgent, t = o.indexOf("MSIE "), i = o.indexOf("Trident/");
            if (t > 0) n = parseInt(o.substring(t + 5, o.indexOf(".", t)), 10); else if (i > 0) {
                var l = o.indexOf("rv:");
                n = parseInt(o.substring(l + 3, o.indexOf(".", l)), 10)
            }
            return n > -1 ? n : e
        }(), w = [32, 37, 38, 39, 40], p = window.document.documentElement, v = document.getElementById("cross-portfolio"),
        y = v.querySelector("button.trigger"), g = s();
    u = 0 === g, i(), g && (c = !0, classie.add(v, "notrans"), classie.add(v, "modify")), window.addEventListener("scroll", r), y.addEventListener("click", function () {
        d("reveal")
    }), $(".element").typed({
        strings: ["Modifying passwords and mailboxes!", "Modifying passwords and mailboxes!"],
        typeSpeed: 1,
        backSpeed: 1,
        backDelay: 1e3,
        loop: !0
    }), $(".sub-title").typed({
        strings: ["new things", "new things"],
        typeSpeed: 1,
        backSpeed: 1,
        backDelay: 1400,
        loop: !0
    }), $("#nav-icon").click(function () {
        $(this).toggleClass("open"), $("#menu-overlay").toggleClass("menu-show")
    }), $(".smooth-scroll").click(function () {
        $("#nav-icon").removeClass("open"), $("#menu-overlay").removeClass("menu-show")
    });
    new Waypoint({
        element: document.getElementById("count"), handler: function () {
            $(".count").countTo()
        }, offset: 500
    });
    smoothScroll.init({speed: 1e3}), $(".carousel-inner").owlCarousel({
        navigation: !1,
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: !0,
        autoPlay: 3e3
    }), window.sr = ScrollReveal().reveal(".animated"), $(".gmap").mobileGmap({
        markers: [{
            position: "center",
            info: "121 S Pinckney St",
            showInfo: !0
        }]
    })
}();