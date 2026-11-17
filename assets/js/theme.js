// Light/dark theme button. With no stored choice the site follows the
// system setting; a click stores the opposite of what is showing now.
(function () {
  var root = document.documentElement;
  var button = document.querySelector(".theme-toggle");
  var system = window.matchMedia("(prefers-color-scheme: dark)");

  function current() {
    return root.dataset.theme || (system.matches ? "dark" : "light");
  }

  function label() {
    if (!button) return;
    var next = current() === "dark" ? "light" : "dark";
    var text = button.dataset["label" + (next === "dark" ? "Dark" : "Light")];
    button.setAttribute("aria-label", text);
    button.title = text;
  }

  // Keep the Giscus comment frame on the same theme as the page.
  function syncComments() {
    var frame = document.querySelector("iframe.giscus-frame");
    if (!frame) return;
    frame.contentWindow.postMessage(
      { giscus: { setConfig: { theme: current() } } },
      "https://giscus.app"
    );
  }

  if (button) {
    button.hidden = false;
    label();
    button.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try { localStorage.setItem("theme", next); } catch (e) {}
      label();
      syncComments();
    });
  }

  system.addEventListener("change", function () {
    if (!root.dataset.theme) { label(); syncComments(); }
  });
})();
