// Redirect if required for dynamic screen size changes
const currentPath = window.location.pathname;
const tabletBreakpoint = 1024;

function redirectOnResize() {
  if (window.innerWidth > tabletBreakpoint) {
    if (["/tags/", "/notes/search/"].includes(currentPath)) {
      window.location.pathname = "/notes/";
    }
  }
}

redirectOnResize();
window.addEventListener("resize", redirectOnResize);

// Allows for tabbing within note textarea elements
const noteContentTabs = () => {
  const noteContent = document.getElementById("note-content");
  if (noteContent) {
    noteContent.addEventListener("keydown", function (e) {
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
  }
};

document.addEventListener("DOMContentLoaded", () => {
  noteContentTabs();
});
