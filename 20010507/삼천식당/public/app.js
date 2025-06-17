// --- 1단계: Firebase 설정 ---
const firebaseConfig = {
    apiKey: "AIzaSyBoz3rca2kYHPT-77FAtN2WfqiM334p1rc",
    authDomain: "bloominglove3000restaurant.firebaseapp.com",
    projectId: "bloominglove3000restaurant",
    storageBucket: "bloominglove3000restaurant.firebasestorage.app",
    messagingSenderId: "1447477736",
    appId: "1:1447477736:web:8719b8c3b9d9cecdf8245d",
    measurementId: "G-QEK3D0QZF8"
};

// --- 2단계: Firebase 초기화 ---
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();
const applicationsRef = db.collection("applications");

// --- 토스트 팝업 기능 ---
function showToast(message, type = 'success') {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) { return; }
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    toastContainer.appendChild(toast);
    setTimeout(() => { toast.classList.add('show'); }, 100);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => { toast.remove(); }, 300);
    }, 3000);
}

// --- 3단계: 페이지 로딩 완료 후 기능 실행 ---
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('apply-form')) {
        setupUserPage();
    } else if (document.getElementById('admin-table')) {
        setupAdminPage();
    }
});


// --- 신청자용 페이지 기능 ---
function setupUserPage() {
    const deadlineNotice = document.getElementById('deadline-notice');
    const deadlineText = deadlineNotice.querySelector('p');
    const applyForm = document.getElementById('apply-form');
    const nameInput = document.getElementById('name-input');
    const applicantListDiv = document.getElementById('applicant-list');
    const confirmedCountSpan = document.getElementById('confirmed-count');
    const copyButton = document.getElementById('copy-button');
    const accountNumberSpan = document.getElementById('account-number');
    const paidCheckbox = document.getElementById('paid-checkbox');
    const applyButton = applyForm.querySelector('button[type="submit"]');
    const searchInput = document.getElementById('search-input');
    
    let fullConfirmedList = [];
    const now = new Date();
    const day = now.getDay();
    const hour = now.getHours();
    const isApplicationOpen = (day === 0 && hour < 15);
    
    if (isApplicationOpen) {
        applyButton.disabled = false;
        applyButton.textContent = '식수 신청하기';
        deadlineNotice.style.display = 'none';
    } else {
        applyButton.disabled = true;
        deadlineNotice.style.display = 'block';
        if (day === 0 && hour >= 15) {
            applyButton.textContent = '신청 시간이 마감되었습니다';
            deadlineText.innerHTML = '오늘 식수 신청이 마감되었습니다.<br>다음 주일에 다시 신청해주세요!';
        } else {
            applyButton.textContent = '주일에만 신청 가능합니다';
            deadlineText.innerHTML = '식수 신청은 주일에만 가능합니다.<br>주일에 다시 방문해주세요!';
        }
    }

    applicationsRef.where("paid", "==", true).orderBy("name", "asc")
        .onSnapshot(
            (snapshot) => {
                confirmedCountSpan.textContent = snapshot.size;
                const names = [];
                snapshot.forEach(doc => { names.push(doc.data().name); });
                fullConfirmedList = names;
                renderList(fullConfirmedList);
            },
            (error) => { 
                console.error("확정 명단 업데이트 중 오류:", error); 
                if (error.code === 'failed-precondition') {
                    alert("명단 정렬에 필요한 데이터베이스 설정이 필요합니다. 개발자 도구(F12)의 콘솔에 보이는 파란색 링크를 클릭하여 색인을 생성해주세요.");
                }
            }
        );

    function renderList(listToRender) {
        applicantListDiv.innerHTML = '';
        if (listToRender.length === 0) {
            applicantListDiv.innerHTML = '<p>아직 식사 확정 명단에 등록된 분이 없습니다.</p>';
        } else {
            listToRender.forEach(name => {
                const p = document.createElement('p');
                p.textContent = name;
                applicantListDiv.appendChild(p);
            });
        }
    }

    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        if (!searchTerm) {
            renderList(fullConfirmedList);
            return;
        }
        const filteredList = fullConfirmedList.filter(name => name.toLowerCase().includes(searchTerm));
        renderList(filteredList);
    });

    applyForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = nameInput.value.trim();
        const hasPaid = paidCheckbox.checked;
        if (!name) return;
        if (!hasPaid) {
            showToast('입금 여부를 체크해주세요.', 'error');
            return;
        }
        const querySnapshot = await applicationsRef.where("name", "==", name).get();
        if (!querySnapshot.empty) {
            showToast('이미 해당 이름으로 신청(또는 대기) 중입니다.', 'error');
            return;
        }
        try {
            await applicationsRef.add({
                name: name,
                paid: hasPaid,
                timestamp: firebase.firestore.FieldValue.serverTimestamp()
            });
            showToast('식수 신청이 접수되었습니다.');
            nameInput.value = '';
            paidCheckbox.checked = false;
        } catch (error) {
            console.error("신청 중 오류 발생:", error);
            alert("신청 처리 중 오류가 발생했습니다.");
        }
    });

    copyButton.addEventListener('click', () => {
        const textArea = document.createElement('textarea');
        textArea.value = accountNumberSpan.textContent.replace(/-/g, ""); 
        document.body.appendChild(textArea);
        textArea.select();
        try {
            document.execCommand('copy');
            showToast('계좌번호가 복사되었습니다.');
        } catch (err) {
            showToast('복사에 실패했습니다. 직접 복사해주세요.', 'error');
        }
        document.body.removeChild(textArea);
    });
}

// --- 관리자용 페이지 기능 ---
function setupAdminPage() {
    const tableBody = document.getElementById('admin-table-body');
    const resetButton = document.getElementById('reset-button');
    const paidCountSpan = document.getElementById('paid-count');

    resetButton.addEventListener('click', async () => {
        if (!confirm("정말로 모든 신청 내역을 삭제하시겠습니까?")) return;
        if (prompt("동의하시면 '초기화'라고 입력해주세요.") !== '초기화') {
            alert("취소되었습니다.");
            return;
        }
        const snapshot = await applicationsRef.get();
        const batch = db.batch();
        snapshot.docs.forEach(doc => batch.delete(doc.ref));
        await batch.commit();
        alert("모든 내역이 초기화되었습니다.");
    });

    applicationsRef.orderBy("timestamp", "asc").onSnapshot(snapshot => {
        tableBody.innerHTML = '';
        let index = 1;
        let paidCount = 0;

        snapshot.forEach(doc => {
            const data = doc.data();
            
            if (data.paid) {
                paidCount++;
            }

            const tr = document.createElement('tr');
            const date = data.timestamp ? data.timestamp.toDate() : new Date();
            const formattedDate = `${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}<br>${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;
            
            // [수정] 상태 표시를 '신청 완료'로 변경합니다. 
            // '미입금 신청'은 현재 로직상 나타나지 않지만, 만약을 위해 다른 이름으로 남겨둡니다.
            tr.innerHTML = `
                <td data-label="순번">${index}</td>
                <td data-label="이름">${data.name}</td>
                <td data-label="신청 시간">${formattedDate}</td>
                <td data-label="상태"><span class="status-paid">${data.paid ? '신청 완료' : '오류(미입금)'}</span></td>
                <td data-label="작업"><button class="delete-btn" data-id="${doc.id}">삭제</button></td>
            `;
            tableBody.appendChild(tr);
            index++;
        });

        paidCountSpan.textContent = paidCount;

        document.querySelectorAll('.delete-btn').forEach(button => {
            button.addEventListener('click', async (e) => {
                const docId = e.target.dataset.id;
                
                if (confirm("이 신청 기록을 정말로 삭제하시겠습니까?")) {
                    try {
                        await applicationsRef.doc(docId).delete();
                        alert("신청 기록이 삭제되었습니다.");
                    } catch (error) {
                        console.error("삭제 중 오류 발생:", error);
                        alert("오류: 기록을 삭제할 수 없습니다.");
                    }
                }
            });
        });
    });
}
