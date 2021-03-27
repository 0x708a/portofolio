const p1 = document.querySelector(".p1");
const p2 = document.querySelector(".p2");
const p3 = document.querySelector(".p3");
const p4 = document.querySelector(".p4");
const back = document.querySelector(".back");

back.addEventListener("click", () => {
    window.location.href = "/";
})

p1.addEventListener("click", () => {
    window.location.href = "/browse/appProfiler/";
})

p2.addEventListener("click", () => {
    window.location.href = "/browse/particleAnimation/";
})

p3.addEventListener("click", () => {
    window.location.href = "/browse/threeJScube/";
})

p4.addEventListener("click", () => {
    window.location.href = "/browse/neuralNetwork";
})
