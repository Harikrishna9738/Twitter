var show_tweets = document.getElementById("show-tweets-button");
show_tweets.addEventListener("click", getRequest);

let tweetsRequest;

function getRequest() {
    tweetsRequest = new XMLHttpRequest();
    if (!tweetsRequest) {
        alert("Could not make request!");
        return false;
    }
    tweetsRequest.onreadystatechange = sendResponse;
    tweetsRequest.open('GET', 'http://127.0.0.1:8000/tweet/');
    tweetsRequest.send();
}

function sendResponse() {
    if (tweetsRequest.readyState === XMLHttpRequest.DONE) {
        if (tweetsRequest.status === 200) {
            let bodyWrapper = document.getElementById("tweet-ui");
            bodyWrapper.innerHTML = '';
            let tweets = JSON.parse(tweetsRequest.responseText);
            for (var i = 0; i < tweets.length; i++) {
                let tweet = tweets[i];
                bodyWrapper.insertAdjacentHTML('afterbegin', "<div uiclass='ui-tweet'>\
                <div class='ui-tweet-top'>\
                <div class='ui-tweet-user-img'></div>\
                <div class='ui-tweet-user-details'>\
                <div class='ui-tweet-user-name'>" + tweet.user.name + "</div>\
                <div class='ui-tweet-tweet-time'>" + tweet.date_time_updated + "</div>\
                </div>\
                </div>\
                <div class='ui-tweet-bottom'>" + tweet.text + "</div>\
                </div>")
            }
        } else {
            alert("Error occured!");
        }
    }
}

var post_tweet = document.getElementById('post-tweets-button');
post_tweet.addEventListener('click', sendPostRequest);

let postRequest;

function sendPostRequest() {
    postRequest = new XMLHttpRequest();
    if (!postRequest) {
        alert("Could not make request!");
        return false;
    }
    postTweet = document.getElementById('tweet-text').value;
    postRequest.onreadystatechange = ShowPostRequestStatus;
    postRequest.open('POST', "http://127.0.0.1:8000/tweet/create/")
    postRequest.setRequestHeader("content-type", "application/json;charset=UTF-8");
    let body = JSON.stringify({
        user: 1,
        text: postTweet,
    });
    postRequest.send(body);
}

function ShowPostRequestStatus() {
    if (postRequest.readyState === XMLHttpRequest.DONE) {
        if (postRequest.status === 201) {
            alert("Tweet successful!");
        } else {
            alert("Tweet failed!");
        }
    }
}