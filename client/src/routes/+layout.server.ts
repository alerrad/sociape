import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./login/$types";

export const load = async ({ cookies }): PageServerLoad => {
    if (cookies.get("token")) {
        // check token here
        throw redirect(308, "/edit");
    }
}