//문제1: 타이머 2개 비교하기,
//다음 코드를 실행하면 어떤 순서로 출력될까요?

console.log("시작");
setTimeout(() => console.log("타이머 A"), 100);
setTimeout(() => console.log("타이머 B"), 50);
console.log("중간");
setTimeout(() => console.log("타이머 C"), 0);
console.log("끝");

// 예상 답:  타이머C , 타이머B , 타이머A 순으로 출력

//////////////////////////////////////////////////////


//문제2: 직접 구현하기,
//다음과 같은 순서로 출력되도록 코드를 완성하세요.

// 원하는 출력:
// 준비
// 시작
// 첫번째 작업 완료
// 두번째 작업 완료
// 모든 작업 끝

// [코드 템플릿]
console.log("준비");

setTimeout(() => {
    console.log("첫번째 작업 완료");
}, 0);

console.log("시작");

setTimeout(() => {
    console.log("두번째 작업 완료");
}, 50);

setTimeout(() => {
    console.log("모든 작업 끝");
}, 100);


//////////////////////////////////////////////////////////


// 문제3: 함수 + setTimeout 조합,
// 다음 코드의 실행 순서를 예측해보세요.
function 작업A() {
    console.log("작업A 시작");
    setTimeout(() => {
        console.log("작업A 완료");
    }, 150);
}

function 작업B() {
    console.log("작업B 시작");
    setTimeout(() => {
        console.log("작업B 완료");
    }, 100);
}

console.log("프로그램 시작");
작업A();
작업B();
console.log("프로그램 끝");


// 출력 순서: 프로그램 시작 -> 작업A 시작 -> 작업B 시작 -> 프로그램 끝 -> 작업 B완료 -> 작업 A 완료 