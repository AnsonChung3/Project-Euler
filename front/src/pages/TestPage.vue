<template>
    <div>
        <h1>{{ TITLE }}</h1>
        <q-btn
            label=test
            @click="test"
        />
    </div>
</template>

<script setup>
const TITLE = 'Test Page';

import { api } from 'src/boot/axios.js';

function test() {
    api.get('api/test')
        .then(response => {
            localStorage.setItem('list_of_primes_357', response.data)
        })
}

// function task () {
//     localStorage.setItem('euler_python_response', 'Answer is { "data": 23, "status": 200, "statusText": "OK", "headers": { "connection": "close", "content-length": "2", "content-type": "text/plain; charset=utf-8", "date": "Sat, 08 Jun 2024 18:23:30 GMT", "server": "Python/3.12 aiohttp/3.9.5", "vary": "Accept-Encoding", "x-powered-by": "Express" }, "config": { "url": "api/PE_question_1", "method": "get", "headers": { "Accept": "application/json, text/plain, */*" }, "baseURL": "", "transformRequest": [ null ], "transformResponse": [ null ], "timeout": 0, "xsrfCookieName": "XSRF-TOKEN", "xsrfHeaderName": "X-XSRF-TOKEN", "maxContentLength": -1, "maxBodyLength": -1, "transitional": { "silentJSONParsing": true, "forcedJSONParsing": true, "clarifyTimeoutError": false } }, "request": "[object XMLHttpRequest]" }');
// }

// function testPythonDemoHelper () {
//     api.get('api/test_demo_helper')
//     .then(response => {
//         console.log(response)
//     })
// }
</script>
