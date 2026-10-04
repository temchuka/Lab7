var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        // родитель кнопки - блок всего поста с классом one-post
        var post = e.target.parentElement;
        // класс folded добавляется (или убирается) у родителя, а не у кнопки
        post.classList.toggle("folded");
        if (post.classList.contains("folded"))
            e.target.innerHTML = "развернуть";
        else
            e.target.innerHTML = "свернуть";
    });
}
