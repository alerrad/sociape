<script lang="ts">
    import UserLink from "$lib/components/UserLink.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<svelte:head>
    <title>@{data.username} Links</title>
    <meta name="description" content={data.bio} />
</svelte:head>

<main class="prose text-center mx-auto pt-8">
    <h1 class="text-2xl pt-10 text-primary font-bold">@{data.username}</h1>
    <div
        class="w-64 h-64 rounded-full bg-cover bg-center mx-auto my-8 shadow-md relative"
        style="background-image: url({data.photoURL ?? '/moth.gif'})"
    >
        <button class="btn btn-error absolute bottom-1 left-1 rounded-3xl">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 22 22"
                stroke="currentColor"
                ><path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                /></svg
            >
            {data.likes.length}
        </button>
        {#if data.likes.length >= 5}
            <a href="/FAQ" class="absolute bottom-1 right-3" target="_blank">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    x="0px"
                    y="0px"
                    width="40"
                    height="40"
                    viewBox="0 0 48 48"
                >
                    <circle cx="24" cy="24" r="20" fill="#4dd0e1" /><path
                        fill="#fff"
                        d="M22.491,30.69c-0.576,0-1.152-0.22-1.591-0.659l-6.083-6.084c-0.879-0.878-0.879-2.303,0-3.182 c0.878-0.879,2.304-0.879,3.182,0l6.083,6.084c0.879,0.878,0.879,2.303,0,3.182C23.643,30.47,23.067,30.69,22.491,30.69z"
                    /><path
                        fill="#fff"
                        d="M22.491,30.69c-0.576,0-1.152-0.22-1.591-0.659c-0.879-0.878-0.879-2.303,0-3.182l9.539-9.539 c0.878-0.879,2.304-0.879,3.182,0c0.879,0.878,0.879,2.303,0,3.182l-9.539,9.539C23.643,30.47,23.067,30.69,22.491,30.69z"
                    />
                </svg>
            </a>
        {/if}
    </div>
    <h3 class="text-xl">{data.fullname}</h3>
    <p class="text-base my-8 max-w-lg px-4 mx-auto">{data.bio}</p>

    <ul class="list-none flex items-center flex-col mb-12">
        {#each data.links as link}
            <li class="my-2">
                <UserLink icon={link.icon} url={link.url} title={link.title} />
            </li>
        {/each}
    </ul>
</main>
