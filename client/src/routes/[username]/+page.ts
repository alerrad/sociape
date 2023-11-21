import type { PageLoad } from "./$types";
import { error } from "@sveltejs/kit";


export const load = (async ({ params }) => {
    if (params.username === "some-unknown-user") throw error(404, "Not found");
    return {
        username: params.username,
        fullname: "Zhansen Segizbay",
        bio: "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laborum molestiae quos architecto in qui aut commodi fuga sint quo sed tenetur.",
        photoURL: null,
        links: [
            {
                "icon": "youtube",
                "url": "https://youtube.com",
                "title": "My YT channel"
            },
            {
                "icon": "tiktok",
                "url": "https://tiktok.com",
                "title": "My tiktok"
            }
        ],
        likes: 5
    }
}) satisfies PageLoad;