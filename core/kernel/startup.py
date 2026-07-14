"""
=========================================================
AETHER
Startup
=========================================================
"""

from core.kernel.app_controller import ApplicationController


def startup():

    controller = ApplicationController()

    controller.initialize()

    return controller