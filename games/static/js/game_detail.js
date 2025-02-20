document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll("#rating-stars i");
    const ratingInput = document.getElementById("rating-value");
    let currentRating = 0; 

    stars.forEach((star, index) => {
        star.addEventListener("click", function () {
            currentRating = index + 1; 
            ratingInput.value = currentRating;

            updateStars(currentRating);
        });

        star.addEventListener("mouseover", function () {
            updateStars(index + 1); 
        });

        star.addEventListener("mouseout", function () {
            updateStars(currentRating); 
        });
    });

    function updateStars(rating) {
        stars.forEach((s, i) => {
            if (i < rating) {
                s.classList.add("active");
            } else {
                s.classList.remove("active");
            }
        });
    }
});