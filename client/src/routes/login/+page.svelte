<script lang="ts">
    import { enhance } from "$app/forms";
    import { theme } from "$lib/stores/writables";

    let login: boolean = true;

    function toggle_auth() {
        login = !login;
    }
</script>

<svelte:head>
    <title>Sociape - login</title>
    <meta name="description" content="Sociape - login" />
</svelte:head>

<section class="py-40">
    <div class="md:mx-auto max-w-2xl px-3">
        {#if login}
            <h2 class="text-current font-bold text-2xl text-center">Login</h2>
            <form class="my-8 max-w-md mx-auto" use:enhance action="login" method="POST">
                <input
                    type="text"
                    placeholder="Username"
                    class="input w-full my-3"
                    class:bg-slate-700={$theme === "dark"}
                    class:bg-slate-200={$theme === "light"}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    class="input w-full my-3"
                    class:bg-slate-700={$theme === "dark"}
                    class:bg-slate-200={$theme === "light"}
                    required
                />
                <button class="btn btn-primary text-lg mt-4" type="submit"
                    >Log in</button
                >
            </form>
        {:else}
            <h2 class="text-current font-bold text-2xl text-center">
                Create account
            </h2>
            <form class="my-8 max-w-md mx-auto" use:enhance action="register" method="POST">
                <input
                    type="text"
                    placeholder="Username"
                    class="input w-full my-3"
                    class:bg-slate-700={$theme === "dark"}
                    class:bg-slate-200={$theme === "light"}
                    required
                />
                <input
                    type="text"
                    placeholder="Full name"
                    class="input w-full my-3"
                    class:bg-slate-700={$theme === "dark"}
                    class:bg-slate-200={$theme === "light"}
                    required
                />
                <input
                    type="text"
                    placeholder="Email"
                    class="input w-full my-3"
                    class:bg-slate-700={$theme === "dark"}
                    class:bg-slate-200={$theme === "light"}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    class="input w-full my-3"
                    class:bg-slate-700={$theme === "dark"}
                    class:bg-slate-200={$theme === "light"}
                    required
                />
                <button class="btn btn-primary text-lg mt-4" type="submit"
                    >Register</button
                >
            </form>
        {/if}
        <div class="text-center">
            {#if login}
                <p>
                    No account? <button
                        class="font-bold underline"
                        on:click={toggle_auth}>Register</button
                    >
                </p>
            {:else}
                <p>
                    Already have an account? <button
                        class="font-bold underline"
                        on:click={toggle_auth}>Log in</button
                    >
                </p>
            {/if}
        </div>
    </div>
</section>
