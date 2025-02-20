document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll("#rating-stars i");
    const ratingInput = document.querySelector("input[name='ratting']");
    let currentRating = ratingInput.value || 0; // Lấy giá trị ban đầu từ input

    stars.forEach((star) => {
        star.addEventListener("click", function () {
            currentRating = this.getAttribute("data-value"); // Lấy giá trị từ data-value
            ratingInput.value = currentRating; // Cập nhật input ẩn
            updateStars(currentRating);
        });

        star.addEventListener("mouseover", function () {
            updateStars(this.getAttribute("data-value")); // Hiển thị khi hover
        });

        star.addEventListener("mouseout", function () {
            updateStars(currentRating); // Quay lại số sao đã chọn
        });
    });

    function updateStars(rating) {
        stars.forEach((s) => {
            if (s.getAttribute("data-value") <= rating) {
                s.classList.add("active");
            } else {
                s.classList.remove("active");
            }
        });
    }

    updateStars(currentRating); // Cập nhật ban đầu nếu đã có rating
});
