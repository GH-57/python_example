// let x = 3;
// let y = '3';
// console.log(x==y);
// console.log(x===y);

// function add(a, b = 20) {
//     return a + b;
// }
// console.log(add(10));


// const numbers = [2, 4, 6];
// const result = numbers
//     .map(x => x*2)
//     .reduce((sum, current) => sum + current, 0);
// console.log(result);
// // 12*2


// JSON의 특징
 
// 다음 중 JSON의 특징으로 올바른 것은?

// 1. 주석을 사용할 수 있다. (X)
// 2. 키(key)에 따옴표가 필수이다. (O)
// 3. 함수를 값으로 가질 수 있다. (X)
// 4. undefined 값을 허용한다. (X)

// 정답
// 키(key)에 따옴표가 필수이다.
// 의견 보내기
// JSON은 데이터 교환 형식으로 더 엄격한 규칙을 가집니다.
// 키는 반드시 큰따옴표로 감싸야 하며, 문자열도 큰따옴표만 사용 가능합니다.
// 함수, undefined, Symbol 등은 JSON에서 지원하지 않습니다.





// const users = [
//    {name: '라이언', role: 'developer'},
//    {name: '스콘', role: 'designer'},
//    {name: '케리', role: 'developer'}
// ];

// const result = users
//    .filter(user => user.role === 'developer')
//    .map(user => user.name);
// console.log(result);