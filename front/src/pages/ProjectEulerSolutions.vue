<template>
    <div>
        <h1>Project Euler</h1>
        <h2>Here are all the problems that I've solved</h2>
        <p>Select a number to see the question and answer</p>
        <div v-for="i in solved" :key="i" class="display-question-number">
            <q-btn
                :label=i
                @click="getQText(i)"
                outline
                class="question-button"
            />
        </div>
        <div class="question-text-display">
            <div v-for="(text, index) in displayText" :key="index">
                <p>{{ text }}</p>
            </div>
            <q-btn
                v-if="selected !== 0"
                label='show answer'
                @click="fetchAnswer"
                outline
            />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { questionTexts } from 'src/components/QuestionTexts.js';

const solved = [1, 9, 20];
const displayText = ref(['Please select a question number.']);
const selected = ref(0);

function getQText (i) {
    selected.value = i;
    const question = questionTexts.find(question => question.num === i);
    displayText.value = question.text;
}

function fetchAnswer () {
    console.log('boop');
}
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
