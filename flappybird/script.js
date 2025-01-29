// script.js
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let bird = { x: 50, y: 150, radius: 15, velocity: 0, gravity: 0.5, lift: -8 };
let pipes = [];
let frame = 0;
let score = 0;
let gameRunning = true;

function drawBird() {
  ctx.beginPath();
  ctx.arc(bird.x, bird.y, bird.radius, 0, Math.PI * 2);
  ctx.fillStyle = "yellow";
  ctx.fill();
  ctx.closePath();
}

function drawPipes() {
  ctx.fillStyle = "green";
  pipes.forEach((pipe) => {
    ctx.fillRect(pipe.x, 0, pipe.width, pipe.top);
    ctx.fillRect(pipe.x, pipe.bottom, pipe.width, canvas.height - pipe.bottom);
  });
}

function update() {
  if (!gameRunning) return;

  bird.velocity += bird.gravity;
  bird.y += bird.velocity;
  if (bird.y + bird.radius >= canvas.height) gameOver();

  if (frame % 90 === 0) {
    let pipeHeight = Math.random() * (canvas.height / 2);
    pipes.push({
      x: canvas.width,
      width: 40,
      top: pipeHeight,
      bottom: pipeHeight + 120,
    });
  }

  pipes.forEach((pipe) => {
    pipe.x -= 2;
    if (pipe.x + pipe.width < 0) {
      pipes.shift();
      score++;
    }
    if (
      bird.x + bird.radius > pipe.x &&
      bird.x - bird.radius < pipe.x + pipe.width &&
      (bird.y - bird.radius < pipe.top || bird.y + bird.radius > pipe.bottom)
    ) {
      gameOver();
    }
  });

  frame++;
}

function gameOver() {
  gameRunning = false;
  alert("Game Over! Score: " + score);
  document.location.reload();
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawBird();
  drawPipes();
  ctx.fillStyle = "black";
  ctx.fillText("Score: " + score, 10, 20);
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}

document.addEventListener("keydown", (e) => {
  if (e.code === "Space") bird.velocity = bird.lift;
});
document.addEventListener("click", () => (bird.velocity = bird.lift));

loop();
