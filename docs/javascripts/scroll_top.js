// Instant navigation loads each new page without a full reload, and some
// browsers keep the old scroll position. When a new page loads without a
// #section in its address, scroll to the top.
document$.subscribe(function () {
  if (!location.hash) {
    window.scrollTo(0, 0);
  }
});
