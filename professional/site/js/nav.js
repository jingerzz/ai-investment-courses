/* ============================================================
   Shared Navigation — AI-Powered Investment Management
   Inserts nav + footer into any page.
   Usage: <script src="js/nav.js" data-current="week-1"></script>
   ============================================================ */

(function () {
  const pages = [
    { id: "home",          href: "index.html",          label: "Home" },
    { id: "foundations-1", href: "foundations-1.html",   label: "Foundations 1" },
    { id: "foundations-2", href: "foundations-2.html",   label: "Foundations 2" },
    { id: "week-1",        href: "week-1.html",         label: "Week 1" },
    { id: "week-2",        href: "week-2.html",         label: "Week 2" },
    { id: "week-3",        href: "week-3.html",         label: "Week 3" },
    { id: "week-4",        href: "week-4.html",         label: "Week 4" },
    { id: "bonus",         href: "bonus.html",          label: "Bonus" },
    { id: "conclusion",    href: "conclusion.html",     label: "Conclusion" },
  ];

  const script = document.currentScript;
  const current = script ? script.getAttribute("data-current") : "";

  /* --- Build nav --- */
  const nav = document.createElement("nav");
  nav.className = "site-nav";
  nav.innerHTML = `
    <div class="site-nav-inner">
      <a class="brand" href="index.html">AI-Powered Investment Management</a>
      <div class="nav-links">
        ${pages.map(p =>
          `<a href="${p.href}" class="${p.id === current ? 'active' : ''}">${p.label}</a>`
        ).join("")}
      </div>
    </div>
  `;

  /* --- Build footer --- */
  const footer = document.createElement("footer");
  footer.className = "site-footer";
  footer.innerHTML = `
    <div class="site-footer-inner">
      <span class="footer-brand">AI Investment Academy</span>
      <span class="footer-note">Build AI tools. No coding required.</span>
    </div>
  `;

  /* --- Build prev/next --- */
  const idx = pages.findIndex(p => p.id === current);
  if (idx >= 0) {
    const prev = idx > 0 ? pages[idx - 1] : null;
    const next = idx < pages.length - 1 ? pages[idx + 1] : null;
    const pageNav = document.createElement("div");
    pageNav.className = "page-nav";
    pageNav.innerHTML = `
      ${prev ? `<a href="${prev.href}"><div class="nav-label">&larr; Previous</div><div class="nav-title">${prev.label}</div></a>` : '<span></span>'}
      ${next ? `<a href="${next.href}"><div class="nav-label">Next &rarr;</div><div class="nav-title">${next.label}</div></a>` : '<span></span>'}
    `;
    /* Insert before footer */
    document.addEventListener("DOMContentLoaded", () => {
      const content = document.querySelector(".content") || document.querySelector(".content-wide");
      if (content) content.appendChild(pageNav);
    });
  }

  /* --- Insert into page --- */
  document.addEventListener("DOMContentLoaded", () => {
    const wrapper = document.querySelector(".page-wrapper");
    if (wrapper) {
      wrapper.prepend(nav);
      wrapper.appendChild(footer);
    }
  });
})();
