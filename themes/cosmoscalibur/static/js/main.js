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
    var navMenu = document.getElementById("navbar-mobile-menu");
    if (navToggle && navMenu) {
      navToggle.addEventListener("click", function () {
        var expanded = navToggle.getAttribute("aria-expanded") === "true";
        navToggle.setAttribute("aria-expanded", String(!expanded));
        navMenu.classList.toggle("is-open");
      });
    }

    /* ── Post byline: move after <h1> title ── */
    var moveByline = function () {
      var byline = document.querySelector(".post-byline");
      var h1 = document.querySelector(".content section > h1");
      if (byline && h1) {
        h1.after(byline);
        byline.classList.add("is-placed");
      }
    };
    if (window.requestIdleCallback) {
      window.requestIdleCallback(moveByline);
    } else {
      window.requestAnimationFrame(moveByline);
    }

    /* ── Site-scoped Google search (replaces inline script) ── */
    var searchForm = document.getElementById("search-overlay");
    if (searchForm) {
      searchForm.addEventListener("submit", function () {
        var input = document.getElementById("search-input");
        var hidden = document.getElementById("search-q");
        if (input && hidden) {
          var domain = document.documentElement.dataset.searchDomain || "";
          hidden.value = (domain ? "site:" + domain + " " : "") + input.value;
        }
      });
    }

    /* ── Search overlay toggle (mobile) ── */
    var searchTrigger = document.querySelector(
      ".navbar__actions--mobile .search-trigger"
    );
    if (searchTrigger && searchForm) {
      searchTrigger.addEventListener("click", function () {
        var isOpen = searchForm.classList.contains("search-form--overlay");
        if (isOpen) {
          searchForm.classList.remove("search-form--overlay");
          searchForm.style.display = "";
          searchTrigger.setAttribute("aria-expanded", "false");
        } else {
          searchForm.classList.add("search-form--overlay");
          searchForm.style.display = "flex";
          searchTrigger.setAttribute("aria-expanded", "true");
          var input = searchForm.querySelector("input[type='search']");
          if (input) input.focus();
        }
      });

      /* Close on click outside */
      document.addEventListener("click", function (e) {
        if (searchForm.classList.contains("search-form--overlay") &&
            !e.target.closest(".search-wrapper") &&
            !e.target.closest(".search-trigger")) {
          searchForm.classList.remove("search-form--overlay");
          searchForm.style.display = "";
          searchTrigger.setAttribute("aria-expanded", "false");
        }
      });

      /* Close on Escape */
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && searchForm.classList.contains("search-form--overlay")) {
          searchForm.classList.remove("search-form--overlay");
          searchForm.style.display = "";
          searchTrigger.setAttribute("aria-expanded", "false");
          searchTrigger.focus();
        }
      });
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
            .getPropertyValue("--navbar-tier1-height")
        ) || 3.5;
        var tier2Rem = parseFloat(
          getComputedStyle(document.documentElement)
            .getPropertyValue("--navbar-tier2-height")
        ) || 2.25;
        var offset = (navbarRem + tier2Rem) * rootFontSize + 24;

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

    /* ── Code block copy button (replaces sphinx_copybutton) ── */
    var codeBlocks = document.querySelectorAll(".highlight pre");
    for (var cb = 0; cb < codeBlocks.length; cb++) {
      (function (pre) {
        var btn = document.createElement("button");
        btn.className = "copy-btn";
        btn.setAttribute("aria-label", "Copy code");
        btn.setAttribute("title", "Copy");
        btn.textContent = "📋";

        btn.addEventListener("click", function () {
          var code = pre.textContent || pre.innerText;
          // Strip leading $ or >>> prompts (common in shell/Python examples)
          code = code.replace(/^\s*(\$|>>>)\s?/gm, "");
          navigator.clipboard.writeText(code).then(function () {
            btn.textContent = "✅";
            btn.setAttribute("aria-label", "Copied!");
            setTimeout(function () {
              btn.textContent = "📋";
              btn.setAttribute("aria-label", "Copy code");
            }, 2000);
          });
        });

        // Wrap pre in relative container for button positioning
        var wrapper = pre.parentNode;
        if (wrapper && wrapper.classList.contains("highlight")) {
          wrapper.style.position = "relative";
          wrapper.appendChild(btn);
        }
      })(codeBlocks[cb]);
    }
  });
})();
