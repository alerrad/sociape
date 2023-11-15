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

export const theme: Writable<string> = writable("dark");
export const user: Writable<User | null> = writable(null);