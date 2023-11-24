<script lang="ts">
    import { theme } from "$lib/stores/writables";
    import { enhance } from "$app/forms";
</script>

<svelte:head>
    <title>Sociape - register</title>
    <meta name="description" content="Sociape - register" />
</svelte:head>

<section class="py-40">
    <div class="mx-auto max-w-2xl px-3">
        <h2 class="text-current font-bold text-2xl text-center">
            Create account
        </h2>
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
                type="text"
                placeholder="Full name"
                class="input w-full my-3"
                class:bg-slate-700={$theme === "dark"}
                class:bg-slate-200={$theme === "light"}
                name="fullname"
                required
            />
            <input
                type="text"
                placeholder="Email"
                class="input w-full my-3"
                class:bg-slate-700={$theme === "dark"}
                class:bg-slate-200={$theme === "light"}
                name="email"
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
                >Register</button
            >
        </form>
        <div class="text-center">
            <p>
                Already have account? <a href="/login" class="link font-medium"
                    >Log in</a
                >
            </p>
        </div>
    </div>
</section>
