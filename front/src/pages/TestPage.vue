<template>
    <div>
        <h1>{{ TITLE }}</h1>
        <q-btn
            label="test"
            @click="testPythonDemoHelper"
        />
    </div>
</template>

<script setup>
const TITLE = 'Test Page';

import { api } from 'src/boot/axios.js';

function testPythonDemoHelper () {
    api.get('api/test_demo_helper')
    .then(response => {
        console.log(response)
    })
}
</script>
