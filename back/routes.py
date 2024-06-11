import views
import math

def setup_routes(app):
    app.router.add_route("GET", "/test", views.test)
    app.router.add_route("GET", "/test_demo_helper", views.test_demo_helper)
    app.router.add_route("GET", "/PE_question_1", views.PE_question_1)
    app.router.add_route("GET", "/PE_question_2", views.PE_question_2)
    app.router.add_route("GET", "/PE_question_3", views.PE_question_3)
    app.router.add_route("GET", "/PE_question_4", views.PE_question_4)
    app.router.add_route("GET", "/PE_question_5", views.PE_question_5)
    app.router.add_route("GET", "/PE_question_6", views.PE_question_6)
    app.router.add_route("GET", "/PE_question_7", views.PE_question_7)
    app.router.add_route("GET", "/PE_question_8", views.PE_question_8)
    app.router.add_route("GET", "/PE_question_10", views.PE_question_10)
    app.router.add_route("GET", "/PE_question_11", views.PE_question_11)
    app.router.add_route("GET", "/PE_question_12", views.PE_question_12)