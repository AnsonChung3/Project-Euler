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
                label="test text"
                @click="testText"
            />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const TITLE = 'Hello! This is template page!';
const INPUT = ref(undefined);
const DISPLAY = ref('Display is empty');

function testText () {
    DISPLAY.value = 'test';
}

</script>

<style scoped>
</style>
