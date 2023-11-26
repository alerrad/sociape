import { redirect } from "@sveltejs/kit";
import { API_HOST } from "$env/static/private";


export const actions = {
    default: async ({ request, fetch, cookies }) => {
        const form_data: FormData = await request.formData();

        const req_body = {
            username: form_data.get("username"),
            password: form_data.get("password"),
        }

        const response = await fetch(API_HOST + "/api/user/login",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(req_body)
            });
        
        const res = await response.json();

        if (res.success) {
            cookies.set("token", res.token);
            cookies.set("user", JSON.stringify(res.data));
            throw redirect(303, "/edit");
        }

        return {
            "success": false,
            "message": "username or password incorrect!"
        }
    },
}