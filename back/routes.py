import views

def setup_routes(app):
    app.router.add_route("GET", "/test", views.test)
    app.router.add_route("GET", "/test_demo_helper", views.test_demo_helper)