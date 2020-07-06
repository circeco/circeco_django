function toggleFav(btn, shopId, csrf) {
    let x = btn.firstElementChild;
    let isFavourite = x.innerHTML.trim() === "star";
    if (!isFavourite) {
        $.ajax({
            type: "PUT",
            url: `/fav/add/${shopId}/ws`,
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrf);
            },
            success: function (data, status, xhr) {
                x.innerHTML = "star";
            }
        })
    } else {
        $.ajax({
            type: "PUT",
            url: `/fav/remove/${shopId}/ws`,
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrf);
            },
            success: function (data, status, xhr) {
                x.innerHTML = "star_border";
            }
        })
    }
}