async function sendScore(gameId, userId, score) {
    const url = "http://127.0.0.1:8000/games/API/leaderboard/";  // Kiểm tra lại URL
    const data = { games: gameId, users: userId, score: score };

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer YOUR_ACCESS_TOKEN"  // Nếu cần xác thực
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Lỗi: ${response.status} - ${response.statusText}`);
        }

        const result = await response.json();
        return result;

    } catch (error) {
        return null;
    }
}

// Gọi hàm để gửi điểm
sendScore(115, 1, 100);
