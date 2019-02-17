.PHONY: init assets

init:
	pip install -r requirements.txt

assets:
	yarn install
	rm -rf ./app/static
	mkdir -p ./app/static
	cp -fr ./node_modules/font-awesome/fonts ./app/static
	cp -fr ./app/assets/images ./app/static
	cp -fr ./app/assets/downloads ./app/static/downloads
