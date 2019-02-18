from app import create_app, config

app = create_app(config.base_config)

if __name__ == "__main__":
    app.run()
