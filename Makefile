.PHONY: init assets

init:
	pip install -r requirements.txt

assets:
	rm -rf ./app/static
	mkdir -p ./app/static
	cp -fr ./app/assets/images ./app/static
	cp -fr ./app/assets/downloads ./app/static/downloads
