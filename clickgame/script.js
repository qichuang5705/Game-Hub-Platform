const target = document.getElementById("target");
const scoreElement = document.getElementById("score");
const timeElement = document.getElementById("time");
const restartButton = document.getElementById("restart");

let score = 0;
let timeLeft = 30;
let gameInterval;
let moveInterval;

// Tạo vị trí ngẫu nhiên cho ô vuông
function moveTarget() {
  const gameArea = document.getElementById("game");
  const maxX = gameArea.offsetWidth - target.offsetWidth;
  const maxY = gameArea.offsetHeight - target.offsetHeight;
  const randomX = Math.floor(Math.random() * maxX);
  const randomY = Math.floor(Math.random() * maxY);
  target.style.left = `${randomX}px`;
  target.style.top = `${randomY}px`;
}

// Tăng điểm khi nhấn vào ô vuông
target.addEventListener("click", () => {
  score++;
  scoreElement.textContent = score;
  moveTarget();
});

// Bắt đầu trò chơi
function startGame() {
  score = 0;
  timeLeft = 30;
  scoreElement.textContent = score;
  timeElement.textContent = timeLeft;

  moveTarget(); // Hiển thị ô vuông ngay lập tức
  moveInterval = setInterval(moveTarget, 1000); // Di chuyển ô vuông mỗi giây
  gameInterval = setInterval(() => {
    timeLeft--;
    timeElement.textContent = timeLeft;
    if (timeLeft <= 0) {
      endGame();
    }
  }, 1000);
}

// Kết thúc trò chơi
function endGame() {
  clearInterval(gameInterval);
  clearInterval(moveInterval);
  alert(`Trò chơi kết thúc! Điểm của bạn là: ${score}`);
}

// Khởi động lại trò chơi
restartButton.addEventListener("click", () => {
  clearInterval(gameInterval);
  clearInterval(moveInterval);
  startGame();
});

// Bắt đầu trò chơi khi tải trang
startGame();
