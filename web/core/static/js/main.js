// Redirect if required for dynamic screen size changes
const currentPath = window.location.pathname;
const tabletBreakpoint = 1024;

function redirectOnResize() {
  if (window.innerWidth > tabletBreakpoint) {
    if (currentPath === "/tags/") {
      window.location.pathname = "/notes/";
    }
  }
}

redirectOnResize();
window.addEventListener("resize", redirectOnResize);

// Respect system prefs if available
document.addEventListener("DOMContentLoaded", () => {
  const root = document.documentElement;
  const body = document.getElementById("app");
  const userTheme = body.getAttribute("data-theme");

  // Apply theme based on user preference
  if (userTheme === "system") {
    const prefersDarkMode = window.matchMedia(
      "(prefers-color-scheme: dark)"
    ).matches;
    if (prefersDarkMode) {
      root.classList.add("dark");
    }

    // Listen for system preference changes
    window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", (e) => {
        if (e.matches) {
          root.classList.add("dark");
        } else {
          root.classList.remove("dark");
        }
      });
  }
});

// Allow tabs within note textareas
document
  .getElementById("note-content")
  .addEventListener("keydown", function (e) {
    if (e.key === "Tab") {
      e.preventDefault();
      const start = this.selectionStart;
      const end = this.selectionEnd;

      // Insert tab character at the caret position
      this.value =
        this.value.substring(0, start) + "\t" + this.value.substring(end);

      // Move the caret after the tab character
      this.selectionStart = this.selectionEnd = start + 1;
    }
  });
