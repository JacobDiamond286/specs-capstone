let reviewPost = document.getElementById('review-post')
let reviewButton = document.getElementById('show-review')
let eldenRing = document.getElementById('show-elden')
console.log("Java Connected")

function onButtonClick(){
    console.log(reviewPost.className == 'hide')
    if (reviewPost.className == 'hide'){
        reviewPost.className = "show";
    } else {
        reviewPost.className = "hide";
    }
}

function eR(){
    if (eldenRing.className == 'hide'){
        eldenRing.className = 'show';
    } else {
        eldenRing.className = 'hide';
    }
}





reviewButton.addEventListener('click', onButtonClick)