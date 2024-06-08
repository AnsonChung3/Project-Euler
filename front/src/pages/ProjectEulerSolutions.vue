<template>
    <div>
        <h1>Project Euler</h1>
        <h2>Here are all the problems that I've solved</h2>
        <p>Select a number to see the question and answer</p>
        <div v-for="i in solved" :key="i" class="display-question-number">
            <q-btn
                :label=i
                outline
                class="question-button"
            />
        </div>
        <div class="question-text-display">{{ questionText }}</div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const solved = [1, 9, 20]
const questionText = ref('Please select a question number.')
</script>

<style scoped>
.display-question-number {
    display: inline
}
.question-button {
    margin-right: 1%
    /* display: inline */
}
.question-text-display {
    border: 2px solid #93a1a1;
    min-height: 50px;
    margin-top: 1%;
    padding: 1%
}
</style>
