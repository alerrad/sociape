import { redirect } from "@sveltejs/kit";
import { Axios } from "axios";

export async function load({ cookies }) {
    if (cookies.get("token")) {
        throw redirect(308, "/edit");
    }
}

export const actions = {
    login: async (event) => {

    },
    register: async (event) => {

    }
}