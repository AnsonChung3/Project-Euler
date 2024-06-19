import views
import math

def setup_routes(app):
    app.router.add_route("GET", "/test", views.test)
    app.router.add_route("GET", "/test_demo_helper", views.test_demo_helper)
    app.router.add_route("GET", "/PE_question_81", views.PE_question_81)
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
    app.router.add_route("GET", "/PE_question_13", views.PE_question_13)
    app.router.add_route("GET", "/PE_question_14", views.PE_question_14)
    app.router.add_route("GET", "/PE_question_15", views.PE_question_15)
    app.router.add_route("GET", "/PE_question_16", views.PE_question_16)
    app.router.add_route("GET", "/PE_question_17", views.PE_question_17)
    app.router.add_route("GET", "/PE_question_18", views.PE_question_18)
    app.router.add_route("GET", "/PE_question_67", views.PE_question_67)
    app.router.add_route("GET", "/PE_question_20", views.PE_question_20)
    app.router.add_route("GET", "/PE_question_22", views.PE_question_22)
    app.router.add_route("GET", "/PE_question_28", views.PE_question_28)
    app.router.add_route("GET", "/PE_question_36", views.PE_question_36)
    app.router.add_route("GET", "/PE_question_41", views.PE_question_41)