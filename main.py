"""App starting point"""

from app import create_app


APP = create_app('config')

if __name__ == '__main__':
    APP.run('0.0.0.0')
