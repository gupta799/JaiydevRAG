from app import create_app

app = create_app('config.config.Config')

if __name__ == '__main__':
    app.run()