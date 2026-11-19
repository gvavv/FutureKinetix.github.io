const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
const navGroups = [...document.querySelectorAll('.nav-group')];
function closeMenu() {
  toggle.setAttribute('aria-expanded', 'false');
  nav.classList.remove('is-open');
  navGroups.forEach(group => { group.removeAttribute('open'); });
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('is-open', open);
});
nav.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    if (toggle.getAttribute('aria-expanded') === 'true' || navGroups.some(group => group.open)) {
      closeMenu();
      toggle.focus();
    }
  }
});
document.addEventListener('click', event => {
  if (!event.target.closest('.header')) closeMenu();
});
matchMedia('(min-width: 1200px)').addEventListener('change', closeMenu);
document.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
  const status = document.querySelector('.copy-status');
  try { await navigator.clipboard.writeText(button.dataset.copy); status.textContent = 'Email скопирован'; }
  catch { status.textContent = 'Email: ' + button.dataset.copy; }
}));

const revealItems = document.querySelectorAll('.hero__copy, .hero__visual, .section, .direction, .editorial-card, .case-card, .config-card, .module-card, .use-cases article');
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealItems.forEach(item => {
    item.classList.add('reveal');
    revealObserver.observe(item);
  });
}
