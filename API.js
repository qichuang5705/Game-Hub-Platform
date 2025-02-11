async function sendScore(gameId, userId, score) {
    const url = "http://127.0.0.1:8000/games/API/leaderboard/";  
    const data = { games: gameId, users: userId, score: score };

    // Lấy CSRF Token từ meta
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken,  // Thêm CSRF Token
                "Authorization": "Bearer YOUR_ACCESS_TOKEN"  // Nếu cần xác thực
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Lỗi: ${response.status} - ${response.statusText}`);
        }

        const result = await response.json();
        console.log("Gửi điểm thành công:", result);
        return result;

    } catch (error) {
        console.error("Lỗi khi gửi điểm:", error);
        return null;
    }
}

// Gọi hàm để gửi điểm
sendScore(115, 1, 100);
