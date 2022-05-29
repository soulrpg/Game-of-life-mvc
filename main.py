"""Game of life MVC - main.py"""

from app import App
from controllers.graphic_controller import GraphicController


def main():
    """Main function"""
    app = App(GraphicController())
    app.run()


if __name__ == '__main__':
    main()
