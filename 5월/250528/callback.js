// *비동기 제어
// const user = {};

// setTimeout(() => {
//     user.name = "weniv";
// }, 0);

// console.log(user);

// *콜백함수
// 다른 함수의 인자로 전달되어서 특정 함수의 인자로 실행되는 것

const user = {};

// function setUser(callback) {
//     setTimeout(() => {
//         user.name = "weniv";
//         callback(user);
//     }, 0);
// }

function printUser(user) {
    console.log(user);
}

// setUser(printUser);
// setUser((user) => console.log(user));

function setUser(callback) {
    setTimeout(() => {
        user.name = "weniv";
        user.age = 20;
        callback(user)
    }, 0);
}

function roleCheck(user, callback) {
    setTimeout(() => {
        if (user.age >= 20) {
            user.role = "성인";
        } else {
            user.role = "학생";
        }
        callback(user);
    }, 1000);
}

setUser((user) => roleCheck(user, printUser));

// 콜백 지옥
func1(function(result1) {
    func2(result1, function (result2) {
        func3(result2, function (result3) {
            // 계속되는 중첩...
        });
    });
});