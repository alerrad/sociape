<script lang="ts">
    import FaqAnswer from "$lib/components/FAQAnswer.svelte";
</script>

<svelte:head>
    <title>Sociape - FAQ</title>
    <meta name="description" content="Sociape - Frequently asked questions">
</svelte:head>

<main class="py-20 px-3">
    <div class="max-w-3xl mx-auto">
        <h1 class="text-4xl text-primary font-bold py-2 border-b-2 text-center">FAQ</h1>
        <FaqAnswer question="How to get verified mark?" answer="Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur eveniet cupiditate ipsum est tempora, labore eum unde sed, maiores, perspiciatis recusandae commodi maxime voluptates dignissimos vero earum assumenda quis accusantium!"/>
        <FaqAnswer question="How many links can I add?" answer="Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur eveniet cupiditate ipsum est tempora, labore eum unde sed, maiores, perspiciatis recusandae commodi maxime voluptates dignissimos vero earum assumenda quis accusantium!"/>
        <FaqAnswer question="Why am I getting 404 page?" answer="It might be because of a high load of the server (it times out requests) and you should come back later. Or the user you were trying to search for does not exist!"/>
        <a href="/" class="btn btn-primary font-semibold mt-6 text-lg">Go back</a>
    </div>
</main>