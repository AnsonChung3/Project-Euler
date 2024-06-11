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
                :label='fetchButtontext'
                @click="fetchAnswer"
                :disable='disableFetch'
                outline
            />
            <p v-if="answerText !== 0" class="answer">
                Answer is {{ answerText }}
            </p>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { api } from 'src/boot/axios.js';
import { questionTexts } from 'src/components/QuestionTexts.js';

const solved = questionTexts.map(questions => questions.num);
const displayText = ref(['Please select a question number.']);
const disableFetch = ref(false);
const fetchButtontext = computed(() => { return disableFetch.value ? 'Fetching answer...' : 'Show Answer' });
const selected = ref(0);
const answerText = ref(0)

function getQText (i) {
    answerText.value = 0;
    selected.value = i;
    const question = questionTexts.find(question => question.num === i);
    displayText.value = question.text;
}

function fetchAnswer () {
    disableFetch.value = !disableFetch.value;
    api.get(`api/PE_question_${selected.value}`)
    .then(response => {
        answerText.value = response.data;
        disableFetch.value = !disableFetch.value;
    })
}
</script>

<style scoped>
.display-question-number {
    display: inline
}
.question-button {
    margin: 0% 1% 1% 0%
}
.question-text-display {
    border: 2px solid #93a1a1;
    min-height: 50px;
    margin-top: 1%;
    padding: 3%
}
.answer {
    margin-top: 2%
}
</style>
