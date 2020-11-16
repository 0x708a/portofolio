const p1 = document.querySelector(".p1");
const p2 = document.querySelector(".p2");
const back = document.querySelector(".back");

back.addEventListener("click", () => {
    window.location.href = "/";
})

p1.addEventListener("click", () => {
    window.location.href = "/browse/appProfiler/"
})
