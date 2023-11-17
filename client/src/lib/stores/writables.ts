import { browser } from "$app/environment";
import { writable, type Writable } from "svelte/store";

interface Link {
    icon: string,
    title: string,
    url: string,
}

interface User {
    username: string,
    bio: string,
    links: Array<Link>,
    verified: boolean,
}

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
export const user: Writable<User | null> = writable(null);