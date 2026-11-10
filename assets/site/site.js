const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
function closeMenu() { toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); }
toggle.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open); });
nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape') { if (toggle.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } } });
document.addEventListener('click', event => { if (!event.target.closest('.header')) closeMenu(); });
matchMedia('(min-width: 1000px)').addEventListener('change', closeMenu);
document.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
  const status = document.querySelector('.copy-status');
  try { await navigator.clipboard.writeText(button.dataset.copy); status.textContent = 'Email скопирован'; }
  catch { status.textContent = 'Email: ' + button.dataset.copy; }
}));
