(function() {
  // Scroll reveal animation
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    document.querySelectorAll('.card, .timeline__item, .facts__card').forEach(function(el) {
      observer.observe(el);
    });
  }

  // Mobile tap handler for flip cards
  document.querySelectorAll('.card').forEach(function(card) {
    card.addEventListener('click', function() {
      card.classList.toggle('card--flipped');
    });
  });
})();
