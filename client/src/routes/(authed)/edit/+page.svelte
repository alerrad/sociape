<script lang="ts">
  import { page } from "$app/stores";
  import { writable } from "svelte/store";

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
</script>

<main class="py-20">
  <div class="max-w-xl mx-auto text-center">
    <h1 class="text-4xl">@Alerrad</h1>
    <h3>You can edit your page here</h3>
    <div
      class="w-52 h-52 rounded-full bg-cover bg-center mx-auto my-8 shadow-md relative"
      style="background-image: url('/moth.gif')"
    />
    <span class="my-8">
      Upload new avatar
      <input type="file" class="file-input w-full max-w-xs" />
    </span>
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
        <button type="submit" class="btn btn-success block">Add Link</button>

        <button type="button" class="btn btn-xs my-4" on:click={cancelLink}
          >Cancel</button
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
