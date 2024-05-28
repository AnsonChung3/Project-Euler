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
        <q-btn
            label="test docker"
            @click="test"
        />
    </div>
</template>

<script setup>
import { ref } from 'vue';

const TITLE = 'Hello! This is template page!';
const INPUT = ref(undefined);

</script>

<style scoped>
</style>
