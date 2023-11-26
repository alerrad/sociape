import { browser } from "$app/environment";
import { writable } from "svelte/store";

// Custom theme tracking store
function themeTracker(defaultTheme: string) {
    const { subscribe, update } = writable(browser && localStorage.getItem("theme") || defaultTheme);
    
    function toggleTheme() {
        update((theme) => {
            const upd = theme === "dark" ? "light" : "dark";
            localStorage.setItem("theme", upd);
            return upd;
        });
    }

    return {
        subscribe,
        toggleTheme,
    }
}

export const theme = themeTracker("dark");