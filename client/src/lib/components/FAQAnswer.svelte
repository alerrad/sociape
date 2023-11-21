<script lang="ts">
    export let question: string;
    export let answer: string;
</script>

<div class="mt-8">
    <h2 class="my-6 text-2xl font-medium">{question}</h2>
    <slot>
        <p class="text-base">{answer}</p>
    </slot>
</div>