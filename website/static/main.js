let reviewPost = document.getElementById('review-post')
let reviewButton = document.getElementById('show-review')
let reviewDelete = document.getElementById('review-delete')
console.log("Java Connected")

function onButtonClick(){
    console.log(reviewPost.className == 'hide')
    if (reviewPost.className == 'hide'){
        reviewPost.className = "show";
    } else {
        reviewPost.className = "hide";
    }
}

function deleteReview(reviewId){
    console.log('Clicked')
    fetch('/delete-review', {
        method: 'POST',
        body: JSON.stringify({ reviewId: reviewId})
    }).then((_res) => {
        window.location.href = '/myreviews';
    });
}

// reviewDelete.addEventListener('click', deleteReview)
reviewButton.addEventListener('click', onButtonClick)