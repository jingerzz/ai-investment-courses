/* ============================================================
   Track Toggle — Systematic Trading / Stock Research
   Persists choice in localStorage across pages.
   Usage: include this script on pages with .track-toggle elements.
   ============================================================ */

(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var trackBtns = document.querySelectorAll(".track-btn");
    if (!trackBtns.length) return;

    var saved = localStorage.getItem("course-track") || "systematic";
    activateTrack(saved);

    trackBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var track = this.getAttribute("data-track");
        activateTrack(track);
        localStorage.setItem("course-track", track);
      });
    });

    function activateTrack(track) {
      trackBtns.forEach(function (b) {
        b.classList.toggle("active", b.getAttribute("data-track") === track);
      });
      document.querySelectorAll(".track-content").forEach(function (c) {
        c.classList.toggle("active", c.getAttribute("data-track") === track);
      });
    }
  });
})();
