// *동기적으로 동작하는 코드
// 한 작업이 완료될 때 까지는, 다음 순서는 실행되지X
// 코드의 순서가 보장된다.
// console.log("hello");
// console.log("world");

// *비동기적으로 동작하는 코드
// 한 작업이 완료되기를 기다리지 않고, 바로 실행된다.
// 코드의 순서가 보장되지 않는다.
// 프로그램의 전반적인 성능 향상

// setTimeout(() => {  // setTimeout은 비동기적으로 동작한다
//     console.log("hello");
// }, 1000);
// console.log("world");

// *js의 비동기 처리 방식
setTimeout(() => {   
    console.log("hello");
}, 0);

console.log("world"); 


// *콜 스텍 처리 과정 (함수의 호출과 관련 => '후입선출')
// 콜스택은 작업을 '동기적'으로 처리한다!
const 참깨빵 = () => {
    console.log("Call 참깨빵");
    순쇠고기패티();
    console.log("End 참깨빵");
};

const 순쇠고기패티 = () => {
    console.log("Call 순쇠고기패티");
    특별한소스();
    console.log("End 순쇠고기패티");
};

const 특별한소스 = () => {
    console.log("Call 특별한소스");
    console.log("End 특별한소스");
};

// 참깨빵();
// console.log("---함수 호출 종료----");

