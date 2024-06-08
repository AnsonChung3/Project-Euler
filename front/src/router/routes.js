
const routes = [
    {
        path: "/",
        component: () => import("layouts/MainLayout.vue"),
        children: [
            { path: "", component: () => import("pages/Index.vue") }
        ]
    },
    {
        path: "/template",
        component: () => import("layouts/SolarizedDarkLayout.vue"),
        children: [
            { path: "", component: () => import("pages/PageTemplate.vue") }
        ]
    },
    {
        path: "/test_page",
        component: () => import("layouts/SolarizedDarkLayout.vue"),
        children: [
            { path: "", component: () => import("pages/TestPage.vue") }
        ]
    },
    {
        path: "/Project_Euler_solutions",
        component: () => import("layouts/SolarizedDarkLayout.vue"),
        children: [
            { path: "", component: () => import("pages/ProjectEulerSolutions.vue") }
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
