from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class AboutController(ControllerBase):
    @staticmethod
    def get():
        name = "JC's Travel Blog"
        return render_template('about.html', name=name)