async function getBuku() {
    return fetch("/forum/json_buku/").then((res) => res.json());
}

async function getThreads() {
    return fetch("/forum/json_thread/").then((res) => res.json());
}

async function refreshThreads() {
    document.getElementById("forum-forum").innerHTML = "";
    const threads = await getThreads();
    let htmlString = "";
    threads.forEach((thread) => {
        htmlString += `
            <div class="thread-panel">
                <img src="${thread.fields.img}" alt="Book Cover">
                <p><a href="/forum/posts/${thread.pk}">${thread.fields.name}</a></p>
                <p>${thread.post_amount}</p>
                <p>${thread.last_post}</p>
            </div>
        `;
    });
    document.getElementById("forum-forum").innerHTML = htmlString;
}

function addThread() {
    fetch("/forum/add_thread/", {
        method: "POST",
        body: new FormData(document.querySelector('#thread-form'))
    }).then(refreshThreads);

    document.getElementById("thread-form").reset();
    return false;
}

async function getPosts(id) {
    return fetch(`/forum/json_posts/${id}/`).then((res) => res.json());
}

async function refreshPosts(id) {
    document.getElementById("post-post").innerHTML = "";
    const posts = await getPosts(id);
    let htmlString = "";
    posts.forEach((post) => {
        htmlString += `
            <div class="post-box">
                <p>${post.fields.user}</p>
                <p>${post.fields.body}</p>
            </div>
        `;
    });
    document.getElementById("post-post").innerHTML = htmlString;
}

function addPost() {
    const searchParams = new URLSearchParams(window.location.search);
    const threadId = searchParams.get('id');

    fetch(`/forum/add_post_flutter/${id}/`, {
        method: "POST",
        body: new FormData(document.querySelector('#post-form'))
    }).then(refreshPosts(id));

    document.getElementById("post-form").reset();
    return false;
}

// Initial load
refreshThreads();
