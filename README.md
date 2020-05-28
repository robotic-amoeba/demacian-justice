# demacian-justice
WIP: karma system for gaming communities.

## Development notes

### Start server locally with pipenv:
`pipenv run python demacian_justice/manage.py runserver`

### Run tests locally
`pipenv run ./demacian_justice/manage.py test`

### Run one test
`pipenv run ./demacian_justice/manage.py test karma.test.test_views.KarmaViewsTest.test_vote_existing_summoner`

### Bundle JS code - Webpack
`npm run dev`

## Set this two env variables
RIOT_API_KEY=your_api_key_here
LOGIN_LEVEL=INFO


## Generate requirements file
`pipenv run pip freeze > requirements.txt`
