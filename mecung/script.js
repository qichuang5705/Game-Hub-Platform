const player = document.getElementById("player");
const exit = document.getElementById("exit");
const maze = document.getElementById("maze");
const timerElement = document.getElementById("timer");
const levelElement = document.getElementById("level");
const messageElement = document.getElementById("message");

let walls = [];
let level = 1;
let timer = 0;
let gameInterval;
let timerInterval;
const timeLimit = 30; // Thời gian giới hạn cho mỗi cấp độ (1 phút)

// Tạo mê cung theo cấp độ
function generateMaze(level) {
  walls.forEach((wall) => wall.remove());
  walls = [];

  for (let i = 0; i < level + 3; i++) {
    const wall = document.createElement("div");
    wall.classList.add("wall");

    const wallWidth = Math.random() * 100 + 50;
    const wallHeight = Math.random() * 20 + 20;
    const wallTop = Math.random() * 300 + 50;
    const wallLeft = Math.random() * 300;

    // Tránh chắn lối ra
    if (Math.abs(wallTop - 360) < 50 && Math.abs(wallLeft - 360) < 50) {
      continue;
    }

    wall.style.width = `${wallWidth}px`;
    wall.style.height = `${wallHeight}px`;
    wall.style.top = `${wallTop}px`;
    wall.style.left = `${wallLeft}px`;
    maze.appendChild(wall);
    walls.push(wall);
  }
}

// Kiểm tra va chạm
function checkCollision(newTop, newLeft) {
  return walls.some((wall) => {
    const wallRect = wall.getBoundingClientRect();
    const playerRect = {
      left: maze.offsetLeft + newLeft,
      top: maze.offsetTop + newTop,
      right: maze.offsetLeft + newLeft + player.offsetWidth,
      bottom: maze.offsetTop + newTop + player.offsetHeight,
    };
    return (
      playerRect.left < wallRect.right &&
      playerRect.right > wallRect.left &&
      playerRect.top < wallRect.bottom &&
      playerRect.bottom > wallRect.top
    );
  });
}

// Kiểm tra thắng cuộc
function checkWin(newTop, newLeft) {
  const exitRect = exit.getBoundingClientRect();
  const playerRect = {
    left: maze.offsetLeft + newLeft,
    top: maze.offsetTop + newTop,
    right: maze.offsetLeft + newLeft + player.offsetWidth,
    bottom: maze.offsetTop + newTop + player.offsetHeight,
  };
  return (
    playerRect.left < exitRect.right &&
    playerRect.right > exitRect.left &&
    playerRect.top < exitRect.bottom &&
    playerRect.bottom > exitRect.top
  );
}

// Di chuyển nhân vật
document.addEventListener("keydown", (event) => {
  let newTop = player.offsetTop;
  let newLeft = player.offsetLeft;

  if (event.key === "ArrowUp") newTop -= 20;
  if (event.key === "ArrowDown") newTop += 20;
  if (event.key === "ArrowLeft") newLeft -= 20;
  if (event.key === "ArrowRight") newLeft += 20;

  if (newTop < 0 || newTop + 20 > 400 || newLeft < 0 || newLeft + 20 > 400) {
    return;
  }

  if (!checkCollision(newTop, newLeft)) {
    player.style.top = `${newTop}px`;
    player.style.left = `${newLeft}px`;

    if (checkWin(newTop, newLeft)) {
      clearInterval(gameInterval);
      clearInterval(timerInterval);
      level++;
      messageElement.textContent = `Chúc mừng! Bạn đã qua cấp độ ${
        level - 1
      }! Bắt đầu cấp độ ${level}!`;
      startGame();
    }
  }
});

// Kết thúc trò chơi do hết thời gian
function loseGame() {
  clearInterval(gameInterval);
  clearInterval(timerInterval);
  level = 1; // Trở lại cấp độ 1
  messageElement.textContent = `Bạn đã thua! Trở về cấp độ 1!`;
  setTimeout(startGame, 2000); // Khởi động lại trò chơi sau 2 giây
}

// Bắt đầu trò chơi
function startGame() {
  // Đặt lại nhân vật và lối ra
  player.style.top = "20px";
  player.style.left = "20px";
  exit.style.top = "360px";
  exit.style.left = "360px";

  // Đặt lại thời gian
  timer = 0;
  timerElement.textContent = timer;
  levelElement.textContent = level;

  generateMaze(level);

  // Đếm thời gian và kiểm tra thời gian giới hạn
  timerInterval = setInterval(() => {
    timer++;
    timerElement.textContent = timer;

    if (timer >= timeLimit) {
      loseGame();
    }
  }, 1000);

  // Bắt đầu trò chơi
  gameInterval = setInterval(() => {}, 50);
}

// Bắt đầu khi tải trang
startGame();
