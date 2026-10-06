(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
        target.setAttribute('tabindex', '-1');
        target.focus({ preventScroll: true });
      }
    });
  });

  // Work dropdown: disclosure button. Closes on Escape, outside click, or focus leaving the menu.
  var btn = document.querySelector('.nav-menu-btn');
  if (!btn) return;
  var menu = btn.parentNode;
  function setOpen(open) { btn.setAttribute('aria-expanded', open ? 'true' : 'false'); }
  function isOpen() { return btn.getAttribute('aria-expanded') === 'true'; }
  btn.addEventListener('click', function () { setOpen(!isOpen()); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && isOpen()) { setOpen(false); btn.focus(); }
  });
  document.addEventListener('click', function (e) {
    if (!menu.contains(e.target)) setOpen(false);
  });
  menu.addEventListener('focusout', function (e) {
    if (e.relatedTarget && !menu.contains(e.relatedTarget)) setOpen(false);
  });
})();
