import { redirect } from "@sveltejs/kit";
import type { Actions } from "@sveltejs/kit";

export const actions: Actions = {
    default: async ({ cookies }) => {
        cookies.delete("token", { path: "/" });
        throw redirect(303, "/");
    }
}