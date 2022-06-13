let reviewPost = document.getElementById('review-post')
let reviewButton = document.getElementById('show-review')
console.log("Java Connected")

function onButtonClick(){
    console.log(reviewPost.className == 'hide')
    if (reviewPost.className == 'hide'){
        reviewPost.className = "show";
    } else {
        reviewPost.className = "hide";
    }
}


reviewButton.addEventListener('click', onButtonClick)