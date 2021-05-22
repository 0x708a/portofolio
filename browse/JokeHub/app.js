const back = document.querySelector(".back");
const signup = document.querySelector(".signup");

back.addEventListener("click", () => {
    window.location.href = "/browse";
})

signup.addEventListener("click", () => {
    document.querySelector(".thankyou").textContent = "Thank You!";
    wiindow.location.href = "/browse";
})
