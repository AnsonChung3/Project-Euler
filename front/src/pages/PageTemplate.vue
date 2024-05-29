<template>
    <div>
        <h1>{{ TITLE }}</h1>
        <div>
            <q-input
                v-model="INPUT"
                dark
                outline
            />
            <p>This is what you typed in the v-modle input field above:</p>
            <p>{{ INPUT }}</p>
        </div>
        <div>
            <h2>Display Box</h2>
            <p>{{ DISPLAY }}</p>
        </div>
        <div>
            <q-btn
                label="test Docker Get"
                @click="testDockerGet"
            />
            <q-btn
                label="test text"
                @click="testText"
            />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { api } from 'src/boot/axios.js';

const TITLE = 'Hello! This is template page!';
const INPUT = ref(undefined);
const DISPLAY = ref('Display is empty');

function testText () {
    DISPLAY.value = 'test';
}

function testDockerGet () {
    console.log('test docker get');
    api.get('api/test')
    .then(response => {
        DISPLAY.value = response.data;
    })
    .catch(error => {
        DISPLAY.value = error;
    })
}

</script>

<style scoped>
</style>
