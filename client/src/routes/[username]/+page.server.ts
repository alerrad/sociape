import type { PageServerLoad } from "./$types";
import { API_HOST } from "$env/static/private";
import { error } from "@sveltejs/kit";


export const load = (async ({ params, fetch }) => {
    const username: string = params.username;
    const req = await fetch(API_HOST + "/api/user/" + username);
    const res = await req.json();

    if (!res.success) {
        throw error(404, "Not found!");
    }

    return res.data;
}) satisfies PageServerLoad;