const p1 = document.querySelector(".p1");
const p2 = document.querySelector(".p2");
const back = document.querySelector(".back");

back.addEventListener("click", () => {
    window.location.href = "/_web/";
})

p1.addEventListener("click", () => {
    window.location.href = "/_web/browse/appProfiler/"
})