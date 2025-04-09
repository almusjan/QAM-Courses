document.querySelectorAll('.fav-btn').forEach((btn) => {
    btn.addEventListener('click', async () => {
        let site_id = btn.getAttribute('data-site-id');
        let csrf_token = getCookie('csrftoken');
        const base_url = window.location.origin;
        fetch(`${base_url}/toggle-favorite/${site_id}/`, {
            method: "POST",
            headers: {
                "content-type": "application/json",
                "X-CSRFToken": csrf_token
            }
        }).then(res => res.json())
            .then(res => {
                const is_fav = '<span class="icon-[tabler--heart-filled]"></span>'
                const is_not_fav = '<span class="icon-[tabler--heart]"></span>'
                let fav_count = res.fav_count
                btn.innerHTML = res.is_favorite ? is_fav + fav_count : is_not_fav + fav_count
            })
    })
})


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
