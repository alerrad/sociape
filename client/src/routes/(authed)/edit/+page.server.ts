import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types.js";


export const load: PageServerLoad = async (event) => {
    if (!event.cookies.get("token")) {
        throw redirect(303, "/login");
    }
    return {
        user: JSON.parse(event.cookies.get("user"))
    }
}