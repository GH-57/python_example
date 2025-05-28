const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        // resolve("요청 성공");
        reject("요청 실패");
    }, 1000);
});


// promise.then((response) => {
//     console.log(response);
// });

promise
.then((response) => {
    console.log(response);

})
.catch((error) => {
    console.log(error);
})
.finally(() => {
    console.log("프로미스 종료!");
});











