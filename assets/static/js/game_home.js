document.addEventListener('DOMContentLoaded', function () {
    const gameInfos = document.querySelectorAll('.game_info');
    gameInfos.forEach(gameInfo => {
        const rating = parseFloat(gameInfo.dataset.rating);
        const starsContainer = gameInfo.querySelector('.stars');

        // 
        for (let i = 0; i < Math.floor(rating); i++) {
            const star = document.createElement('i');
            star.classList.add('fa-solid', 'fa-star');
            starsContainer.appendChild(star);
        }

        // 
        if (rating % 1 !== 0) {
            const halfStar = document.createElement('i');
            halfStar.classList.add('fa-solid', 'fa-star-half-stroke');
            starsContainer.appendChild(halfStar);
        }
    });
});
