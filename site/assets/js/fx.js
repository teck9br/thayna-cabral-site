// Dá sombra ao cabeçalho depois do topo. A entrada do topo da página é só CSS (classe .js no <html>).
// Os blocos que surgiam ao rolar foram retirados no redesenho de 05/11/2026.
(function () {
  window.FX = 1;
  var hdr = document.querySelector('.hdr');
  function onScroll() { if (hdr) hdr.classList.toggle('is-scrolled', window.scrollY > 10); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
