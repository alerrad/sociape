<script lang="ts">
    import { theme } from "$lib/stores/writables";
    
    export let icon: string;
    export let url: string;
    export let title: string;
</script>

<a
    href={url}
    class="stack w-72 text-center bg-base-300 flex justify-center items-center p-4 rounded-lg no-underline"
    target="_blank"
>
    <img src={`/${icon}.png`} width="32" height="32" class="w-8" alt={icon} />
    <span
        class="text-lg font-bold"
        class:text-white={$theme === 'dark'}
    >{title}</span>
</a>
