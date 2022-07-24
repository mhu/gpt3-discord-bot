deploy:
	git push heroku master

logs:
	heroku logs --tail
