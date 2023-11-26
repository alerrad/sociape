<script lang="ts">
    import { writable } from "svelte/store";
    import { theme } from "$lib/stores/writables";
    import type { PageServerData } from "./$types";
    import UserLink from "$lib/components/UserLink.svelte";

    let showForm = false;

    const formDefaults = {
        icon: "custom",
        title: "",
        url: "https://",
    };

    const icons = [
        "Twitter",
        "YouTube",
        "TikTok",
        "LinkedIn",
        "GitHub",
        "Custom",
    ];

    let formData = writable(formDefaults);

    function cancelLink() {
        formData.set(formDefaults);
        showForm = false;
    }

    export let data: PageServerData;
</script>

<svelte:head>
    <title>Sociape - edit your page</title>
    <meta name="description" content="Sociape - edit your profile" />
</svelte:head>

<main class="py-20">
    <form action="/logout" method="POST">
        <button class="btn fixed top-1 right-1" type="submit">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="25"
                height="25"
                viewBox="0 0 25 25"
                fill="none"
                stroke={$theme === "light" ? "#333" : "#FFF"}
                stroke-width="2.2"
                stroke-linecap="round"
                stroke-linejoin="round"
                ><path
                    d="M10 3H6a2 2 0 0 0-2 2v14c0 1.1.9 2 2 2h4M16 17l5-5-5-5M19.8 12H9"
                /></svg
            >
        </button>
    </form>
    <div class="max-w-xl mx-auto text-center">
        <h1 class="text-3xl font-semibold text-primary">
            @{data.user.username}
        </h1>
        <h3>You can edit your page here</h3>
        <div
            class="w-52 h-52 rounded-full bg-cover bg-center mx-auto my-8 shadow-md relative"
            style="background-image: url({data.user.avatar !== ''
                ? ''
                : '/moth.gif'})"
        />
        <h2 class="font-semibold text-2xl">{data.user.fullname}</h2>
        <div class="my-10">
            <p class="my-4">Upload new avatar</p>
            <input type="file" class="file-input w-full max-w-xs" />
        </div>
        <ul class="list-none flex items-center flex-col mb-10">
            {#each data.user.links as link}
                <li class="my-2">
                    <UserLink icon={link.icon} url={link.url} title={link.title} />
                </li>
            {/each}
        </ul>
        {#if showForm}
            <form
                on:submit|preventDefault
                class="bg-base-200 p-6 w-full mx-auto rounded-xl"
            >
                <select
                    name="icon"
                    class="select select-sm"
                    bind:value={$formData.icon}
                >
                    {#each icons as icon}
                        <option value={icon.toLowerCase()}>{icon}</option>
                    {/each}
                </select>
                <input
                    name="title"
                    type="text"
                    placeholder="Title"
                    class="input input-sm"
                    bind:value={$formData.title}
                />
                <input
                    name="url"
                    type="text"
                    placeholder="URL"
                    class="input input-sm"
                    bind:value={$formData.url}
                />
                <button type="submit" class="btn btn-success block"
                    >Add Link</button
                >

                <button
                    type="button"
                    class="btn btn-xs my-4"
                    on:click={cancelLink}>Cancel</button
                >
            </form>
        {:else}
            <button
                on:click={() => (showForm = true)}
                class="btn btn-outline btn-info block mx-auto my-4"
            >
                Add a Link
            </button>
        {/if}
    </div>
</main>
