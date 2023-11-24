import { redirect } from "@sveltejs/kit";
import { API_HOST } from "$env/static/private";


export const actions = {
    default: async ({ request, fetch }) => {
        const form_data: FormData = await request.formData();

        const req_body = {
            username: form_data.get("username"),
            fullname: form_data.get("fullname"),
            email: form_data.get("email"),
            password: form_data.get("password"),
        }

        const response = await fetch(API_HOST + "/api/user/register",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(req_body)
            });
        
        const res = await response.json();

        if (res.success) {
            throw redirect(303, "/login");
        }

        return {
            "success": false,
            "message": "username or password incorrect!"
        }
    },
}