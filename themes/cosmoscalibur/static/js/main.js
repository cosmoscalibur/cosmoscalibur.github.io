/**
 * Cosmoscalibur Theme — main.js
 * Vanilla JS (~3 KB). Mobile nav, back-to-top, TOC scroll-spy, search init.
 * Dark-only theme. No dependencies.
 */

(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    /* ── Mobile nav toggle ── */
    var navToggle = document.querySelector(".navbar__toggle");
    var navMenu = document.getElementById("navbar-nav");
    if (navToggle && navMenu) {
      navToggle.addEventListener("click", function () {
        var expanded = navToggle.getAttribute("aria-expanded") === "true";
        navToggle.setAttribute("aria-expanded", String(!expanded));
        navMenu.classList.toggle("is-open");
      });
    }

    /* ── Back to top ── */
    var backBtn = document.querySelector("[data-back-to-top]");
    if (backBtn) {
      var SCROLL_THRESHOLD = 300;
      window.addEventListener(
        "scroll",
        function () {
          if (window.scrollY > SCROLL_THRESHOLD) {
            backBtn.removeAttribute("hidden");
          } else {
            backBtn.setAttribute("hidden", "");
          }
        },
        { passive: true }
      );
    }

    /* ── TOC scroll-spy: highlight current section ──
       Uses scroll listener with requestAnimationFrame.
       Anchor clicks lock the active state via hashchange. */
    var tocSidebar = document.getElementById("toc-sidebar");
    if (tocSidebar) {
      var tocLinks = tocSidebar.querySelectorAll('a[href^="#"]');
      if (tocLinks.length > 0) {
        var headingEntries = [];
        var tocMap = {};
        for (var j = 0; j < tocLinks.length; j++) {
          var hash = tocLinks[j].getAttribute("href");
          var id = hash === "#" ? "" : hash.slice(1);
          var target = id ? document.getElementById(id) : null;
          if (hash === "#" || target) {
            headingEntries.push({ id: id || "__top__", el: target });
            tocMap[id || "__top__"] = tocLinks[j];
          }
        }

        var activeId = "";
        var anchorLock = false; /* True when user clicked a TOC link */
        var rootFontSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
        var navbarRem = parseFloat(
          getComputedStyle(document.documentElement)
            .getPropertyValue("--navbar-height")
        ) || 3.5;
        var offset = navbarRem * rootFontSize + 24;

        function setActive(id) {
          if (id === activeId) return;
          var prev = tocSidebar.querySelector("a.is-active");
          if (prev) {
            prev.classList.remove("is-active");
            var prevLi = prev.closest("li");
            if (prevLi) prevLi.classList.remove("is-active");
          }
          activeId = id;
          if (tocMap[id]) {
            tocMap[id].classList.add("is-active");
            var newLi = tocMap[id].closest("li");
            if (newLi) newLi.classList.add("is-active");
          }
        }

        var ticking = false;
        function updateActiveSection() {
          if (anchorLock) { ticking = false; return; }
          var current = "__top__";
          for (var k = 0; k < headingEntries.length; k++) {
            var entry = headingEntries[k];
            if (!entry.el) continue;
            var rect = entry.el.getBoundingClientRect();
            if (rect.top <= offset) {
              current = entry.id;
            } else {
              break;
            }
          }
          setActive(current);
          ticking = false;
        }

        window.addEventListener("scroll", function () {
          if (!ticking) {
            requestAnimationFrame(updateActiveSection);
            ticking = true;
          }
        }, { passive: true });

        /* Detect actual user scroll (wheel / touch / keyboard) to
           release anchor lock. Programmatic scroll from anchor
           navigation does NOT trigger these events. */
        function releaseAnchorLock() {
          if (anchorLock) {
            anchorLock = false;
            updateActiveSection();
          }
        }
        window.addEventListener("wheel", releaseAnchorLock, { passive: true, once: false });
        window.addEventListener("touchmove", releaseAnchorLock, { passive: true, once: false });
        window.addEventListener("keydown", function (e) {
          var scrollKeys = [32, 33, 34, 35, 36, 38, 40]; /* Space PgUp PgDn End Home Up Down */
          if (scrollKeys.indexOf(e.keyCode) !== -1) releaseAnchorLock();
        });

        /* Anchor click → lock highlight to clicked section */
        function onHashChange() {
          var h = window.location.hash;
          var targetId = h && h !== "#" ? h.slice(1) : "__top__";
          if (tocMap[targetId]) {
            anchorLock = true;
            setActive(targetId);
          }
        }
        window.addEventListener("hashchange", onHashChange);

        /* Also handle clicks directly (for links with href="#") */
        for (var m = 0; m < tocLinks.length; m++) {
          tocLinks[m].addEventListener("click", (function (link) {
            return function () {
              var clickHash = link.getAttribute("href");
              var clickId = clickHash === "#" ? "__top__" : clickHash.slice(1);
              anchorLock = true;
              setActive(clickId);
            };
          })(tocLinks[m]));
        }

        /* On page load: respect existing hash, else scroll-spy */
        if (window.location.hash && window.location.hash !== "#") {
          onHashChange();
        } else {
          updateActiveSection();
        }
      }
    }

    /* ── Sphinx search initialization (no jQuery) ── */
    if (typeof Search !== "undefined" && document.getElementById("search-results")) {
      Search.init();
    }
  });
})();
