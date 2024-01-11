document.addEventListener("DOMContentLoaded", function () {
  const wikilinks = document.querySelectorAll("a[data-wikilink]");

  wikilinks.forEach(function (link) {
    const target = link.getAttribute("data-wikilink");
    link.href = target + ".html"; // Assuming your wikilinks point to other HTML files
    link.addEventListener("click", function (event) {
      event.preventDefault();
      // You can customize the behavior when a wikilink is clicked
      // For example, load the linked content dynamically
      alert("Clicked on wikilink to " + target);
    });
  });
});
