from django.shortcuts import redirect, render
from .models import Game, Leaderboard

def game_list(request):
    # Add logic to retrieve and display the game list
    return render(request, 'games/game_list.html')

def game_leaderboard(request, game_id):
    # Fetch the game and its leaderboard based on game_id
    game = Game.objects.get(id=game_id)
    leaderboard = Leaderboard.objects.filter(game=game).order_by('-score')  # Example ordering
    return render(request, 'games/leaderboard.html', {'game': game, 'leaderboard': leaderboard})
from .forms import ReviewForm  # Assuming you're using a form for submitting reviews

def submit_review(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the review data
            review = form.save(commit=False)
            review.game = game
            review.save()
            return redirect('game_leaderboard', game_id=game.id)  # Redirect to the leaderboard or another page
    else:
        form = ReviewForm()
    return render(request, 'games/submit_review.html', {'form': form, 'game': game})