document.addEventListener("DOMContentLoaded", function () {
  const avatarInput = document.getElementById("game-avatar");
  const avatarPreview = document.getElementById("avatar-preview");
  const gameForm = document.getElementById("game-form");
  const gamesList = document.getElementById("games-list");

  // 🖼 Xử lý chọn avatar
  if (avatarInput) {
    avatarInput.addEventListener("change", function (event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          avatarPreview.src = e.target.result;
          localStorage.setItem("avatar", e.target.result);
        };
        reader.readAsDataURL(file);
      }
    });

    if (localStorage.getItem("avatar")) {
      avatarPreview.src = localStorage.getItem("avatar");
    }
  }

  // 🚀 Lưu game mới
  if (gameForm) {
    gameForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const gameName =
        document.getElementById("game-name").value.trim() || "Chưa có tên";
      const gameDescription =
        document.getElementById("game-description").value.trim() ||
        "Không có mô tả";
      const gameCategory =
        document.getElementById("game-category").value.trim() ||
        "Không xác định";
      const gamePrice =
        document.getElementById("game-price").value.trim() || "0";
      const gameAvatar = localStorage.getItem("avatar") || "default-avatar.png";

      let games = JSON.parse(localStorage.getItem("games")) || [];

      games.push({
        name: gameName,
        description: gameDescription,
        category: gameCategory,
        price: gamePrice,
        avatar: gameAvatar,
      });

      localStorage.setItem("games", JSON.stringify(games));
      localStorage.removeItem("avatar"); // Xóa avatar sau khi lưu
      gameForm.reset();
      avatarPreview.src = "default-avatar.png";
      window.location.href = "games.html"; // Chuyển đến danh sách game
    });
  }

  // 📜 Hiển thị danh sách game
  if (gamesList) {
    let games = JSON.parse(localStorage.getItem("games")) || [];

    if (games.length === 0) {
      gamesList.innerHTML = "<p>Không có game nào được lưu.</p>";
      return;
    }

    games.forEach((game, index) => {
      const gameItem = document.createElement("div");
      gameItem.classList.add("game-item");
      gameItem.innerHTML = `
        <div class="game-card">
          <img src="${game.avatar}" alt="Game Avatar" class="game-avatar">
          <h3><strong>🎮 Tên Game:</strong> <span class="edit-game-name" contenteditable="false">${game.name}</span></h3>
          <p><strong>📄 Mô Tả:</strong> <span class="edit-game-description" contenteditable="false">${game.description}</span></p>
          <p><strong>📑 Thể loại:</strong> <span class="edit-game-category" contenteditable="false">${game.category}</span></p>
          <p><strong>💲 Giá:</strong> <span class="edit-game-price" contenteditable="false">${game.price}</span> VNĐ</p>
          <div class="game-buttons">
              <button class="edit-game" data-index="${index}">✏️ Sửa</button>
              <button class="save-game" data-index="${index}" style="display: none;">💾 Lưu</button>
              <button class="delete-game" data-index="${index}">🗑 Xóa</button>
          </div>
        </div>
      `;
      gamesList.appendChild(gameItem);
    });

    // ✏️ Xử lý khi nhấn "Sửa"
    document.querySelectorAll(".edit-game").forEach((btn) => {
      btn.addEventListener("click", function () {
        const index = this.getAttribute("data-index");
        const gameDiv = this.parentElement.parentElement;

        // Cho phép chỉnh sửa
        gameDiv.querySelector(".edit-game-name").contentEditable = "true";
        gameDiv.querySelector(".edit-game-description").contentEditable =
          "true";
        gameDiv.querySelector(".edit-game-category").contentEditable = "true";
        gameDiv.querySelector(".edit-game-price").contentEditable = "true";

        // Hiển thị nút "Lưu", ẩn nút "Sửa"
        gameDiv.querySelector(".save-game").style.display = "inline-block";
        gameDiv.querySelector(".edit-game").style.display = "none";
      });
    });

    // 💾 Xử lý khi nhấn "Lưu"
    document.querySelectorAll(".save-game").forEach((btn) => {
      btn.addEventListener("click", function () {
        const index = this.getAttribute("data-index");
        const gameDiv = this.parentElement.parentElement;

        // Lưu thông tin đã chỉnh sửa
        games[index].name =
          gameDiv.querySelector(".edit-game-name").innerText.trim() ||
          "Chưa có tên";
        games[index].description =
          gameDiv.querySelector(".edit-game-description").innerText.trim() ||
          "Không có mô tả";
        games[index].category =
          gameDiv.querySelector(".edit-game-category").innerText.trim() ||
          "Không xác định";
        games[index].price =
          gameDiv.querySelector(".edit-game-price").innerText.trim() || "0";

        // Cập nhật localStorage
        localStorage.setItem("games", JSON.stringify(games));

        // Chuyển về trạng thái không chỉnh sửa
        gameDiv.querySelector(".edit-game-name").contentEditable = "false";
        gameDiv.querySelector(".edit-game-description").contentEditable =
          "false";
        gameDiv.querySelector(".edit-game-category").contentEditable = "false";
        gameDiv.querySelector(".edit-game-price").contentEditable = "false";

        // Hiển thị lại nút "Sửa", ẩn nút "Lưu"
        gameDiv.querySelector(".save-game").style.display = "none";
        gameDiv.querySelector(".edit-game").style.display = "inline-block";
      });
    });

    // 🗑 Xóa game
    document.querySelectorAll(".delete-game").forEach((button) => {
      button.addEventListener("click", function () {
        const index = this.getAttribute("data-index");
        games.splice(index, 1);
        localStorage.setItem("games", JSON.stringify(games));
        location.reload();
      });
    });
  }
});
