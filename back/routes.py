import views
import math

def setup_routes(app):
    app.router.add_route("GET", "/test", views.test)
    app.router.add_route("GET", "/test_demo_helper", views.test_demo_helper)
    app.router.add_route("GET", "/PE_question_1", views.PE_question_1)
    app.router.add_route("GET", "/PE_question_2", views.PE_question_2)
    app.router.add_route("GET", "/PE_question_3", views.PE_question_3)