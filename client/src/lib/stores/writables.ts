import { writable, type Writable } from "svelte/store";

export const theme: Writable<string> = writable("dark");