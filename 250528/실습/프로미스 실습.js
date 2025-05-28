// callback을 promise로
const user = {};

function setUser() {
    return new Promise((resolve) => {
        setTimeout(() => {
            user.name = "weniv";
            user.age = 20;
            resolve(user);
        }, 0);
    });
}

function printUser(user) {
    console.log(user);
}

function roleCheck(user) {
    return new Promise((resolve) => {
        setTimeout(() => {
            if (user.age >= 20) {
                user.role = "성인";
            } else {
                user.role = "학생";
            }
            resolve(user);
        }, 0);
    });
}

// setUSer((user) => roleCheck(user, printUser));

// setUser().then((response) => console.log(response));
// setUser()
//     .then(roleCheck)
//     .then((user) => console.log(user));

setUser().then(roleCheck).then(printUser);
