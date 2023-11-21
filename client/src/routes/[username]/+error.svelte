<script lang="ts">
    import { theme } from "$lib/stores/writables";
</script>

<main class="py-40 px-4">
    <div class="max-w-3xl mx-auto">
        <h3
            class="text-base font-bold"
            class:text-slate-300={$theme === "dark"}
            class:text-slate-600={$theme === "light"}
        >
            404 Not found :(
        </h3>
        <h1 class="text-primary text-5xl py-6 font-medium">
            Might be a wrong link?
        </h1>
        <p class="text-base">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi
            aperiam repudiandae ducimus numquam amet quis laboriosam distinctio
            quam ipsa. Saepe ullam in sint vero perferendis nemo, rerum
            obcaecati error placeat.
        </p>
        <a href="/" class="btn btn-warning mt-6 font-medium text-base"
            >Go home</a
        >
        <a href="/FAQ" class="btn btn-secondary font-medium text-base">FAQ</a>
    </div>
</main>
