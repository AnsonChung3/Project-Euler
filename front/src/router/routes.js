
const routes = [
    {
        path: "/",
        component: () => import("layouts/SolarizedDarkLayout.vue"),
        children: [
            { path: "", component: () => import("pages/ProjectEulerSolutions.vue") }
        ]
    },
    {
        path: "/test_page",
        component: () => import("layouts/SolarizedDarkLayout.vue"),
        children: [
            { path: "", component: () => import("pages/TestPage.vue") }
        ]
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: "/:catchAll(.*)*",
        component: () => import("pages/Error404.vue")
    }
];

export default routes;
