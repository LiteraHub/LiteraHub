async function getBuku() {
    return fetch("/forum/get_books_json").then((res) => res.json())
}

async function getThreads() {
    return fetch("/forum/get_threads").then((res) => res.json())
}

async function refreshThreads() {
    document.getElementById("forum-forum").innerHTML = "";
    const threads = await getThreads();
    let htmlString = "";
    threads.forEach((thread) => {
        htmlString += `
            <div class="thread-panel">
            <img src="${thread.book_cover}" alt="Book Cover">
            <p><a href="/forum/threads">${thread.fields.name}</a></p>
            <p>${thread.fields.author}</p>
            <p>${thread.fields.post_amount}</p>
            <p>${thread.fields.last_post}</p>
        </div>
        
            </div>
        `;
    });
    document.getElementById("forum-forum").innerHTML = htmlString;
}
refreshThreads()

function addThread() {
    fetch("/forum/add_thread", {
        method: "POST",
        body: new FormData(document.querySelector('#thread-form'))
    }).then(refreshThreads)

    document.getElementById("thread-form").reset()
    return false
}

async function getPosts() {
    return fetch("/forum/get_post").then((res) => res.json())
}

async function refreshPosts() {
    document.getElementById("post-post").innerHTML = "";
    const posts = await getPosts();
    let htmlString = "";
    posts.forEach((post) => {
        htmlString += `
            <div class="post-box">
                <p>${post.fields.user}</p>
                <p>${post.fields.body}</p>
                <p>"{{ thread.book_cover }}"</p>
            </div>
        `;
    });
    document.getElementById("post-post").innerHTML = htmlString;
}
refreshPosts()

function addPost() {
    fetch("/forum/add_post", {
        method: "POST",
        body: new FormData(document.querySelector('#post-form'))
    }).then(refreshPosts)

    document.getElementById("post-form").reset()
    return false
}