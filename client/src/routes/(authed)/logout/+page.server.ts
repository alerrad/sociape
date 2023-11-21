import { redirect } from "@sveltejs/kit";
import type { Actions } from "@sveltejs/kit";

export const actions: Actions = {
    default: ({ cookies }) => {
        cookies.delete("token", { path: "/" });
        throw redirect(303, "/");
    }
}