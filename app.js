const browse = document.querySelector(".browse");
const ideas = document.querySelector(".ideas");

browse.addEventListener("click", () => {
    window.location.href = "/browse/"
})

ideas.addEventListener("click", () => {
    window.location.href = "/ideas/"
})