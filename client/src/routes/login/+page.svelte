<script lang="ts">
    import { enhance } from "$app/forms";
    import { theme } from "$lib/stores/writables";
</script>

<svelte:head>
    <title>Sociape - login</title>
    <meta name="description" content="Sociape - login" />
</svelte:head>

<section class="py-40">
    <div class="md:mx-auto max-w-2xl px-3">
        <h2 class="text-current font-bold text-2xl text-center">Login</h2>
        <form class="my-8 max-w-md mx-auto" method="POST" use:enhance>
            <input
                type="text"
                placeholder="Username"
                class="input w-full my-3"
                class:bg-slate-700={$theme === "dark"}
                class:bg-slate-200={$theme === "light"}
                name="username"
                required
            />
            <input
                type="password"
                placeholder="Password"
                class="input w-full my-3"
                class:bg-slate-700={$theme === "dark"}
                class:bg-slate-200={$theme === "light"}
                name="password"
                required
            />
            <button class="btn btn-primary text-lg mt-4" type="submit"
                >Log in</button
            >
        </form>
        <div class="text-center">
            <p>No account? <a href="/register" class="font-medium link">Register</a></p>
        </div>
    </div>
</section>
