<template>
    <div>
        <h1>{{ TITLE }}</h1>
        <q-btn
            label="test docker"
            @click="test"
        />
    </div>
</template>

<script setup>
const TITLE = 'Hello! This is template page!';
</script>

<style scoped>
</style>
