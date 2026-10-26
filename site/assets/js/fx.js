// Animações do site: elementos surgem ao rolar e o cabeçalho ganha sombra depois do topo.
// A lista RV precisa ser a mesma do CSS (`.js :is(...)` em index.html): lá eles já começam ocultos,
// antes da primeira pintura, para o texto não aparecer e sumir de novo.
(function () {
  window.FX = 1;
  var RV = '.sec__head>div>*,.sec__head>.lead,.center-head>*,.faq__head>*,.about__txt>*,.cta>*,.steps li,.qa,.grid>*,.pills>*,.related>*,.prose>*,.aside,.cred__card,.marq';
  var hdr = document.querySelector('.hdr');
  function onScroll() { if (hdr) hdr.classList.toggle('is-scrolled', window.scrollY > 10); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  var els = [].slice.call(document.querySelectorAll(RV));
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    els.forEach(function (e) { e.classList.add('in'); });
    return;
  }
  // os que entram juntos na tela aparecem em sequência (0, 90, 180… ms)
  var io = new IntersectionObserver(function (entries) {
    var i = 0;
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      en.target.style.setProperty('--d', Math.min(i++, 5) * 0.09 + 's');
      en.target.classList.add('in');
      io.unobserve(en.target);
    });
  }, { rootMargin: '0px 0px -6% 0px' });
  els.forEach(function (e) { io.observe(e); });
})();
