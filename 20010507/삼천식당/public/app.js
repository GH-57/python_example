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
    const applyForm = document.getElementById('apply-form');
    const nameInput = document.getElementById('name-input');
    const applicantListDiv = document.getElementById('applicant-list');
    const cancelForm = document.getElementById('cancel-form');
    const cancelNameInput = document.getElementById('cancel-name-input');
    const confirmedCountSpan = document.getElementById('confirmed-count');
    const copyButton = document.getElementById('copy-button');
    const accountNumberSpan = document.getElementById('account-number');

    applicationsRef.where("paid", "==", true).orderBy("timestamp", "desc")
        .onSnapshot(
            (snapshot) => {
                applicantListDiv.innerHTML = '';
                confirmedCountSpan.textContent = snapshot.size;

                if (snapshot.empty) {
                    applicantListDiv.innerHTML = '<p>아직 식사 확정 명단에 등록된 분이 없습니다.</p>';
                } else {
                    snapshot.forEach(doc => {
                        const p = document.createElement('p');
                        p.textContent = doc.data().name;
                        applicantListDiv.appendChild(p);
                    });
                }
            },
            (error) => {
                console.error("실시간 확정 명단 업데이트 중 오류 발생!:", error);
            }
        );

    applyForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = nameInput.value.trim();
        if (!name) return;
        const querySnapshot = await applicationsRef.where("name", "==", name).get();
        if (!querySnapshot.empty) {
            showToast('이미 해당 이름으로 신청(또는 대기) 중입니다.', 'error');
            return;
        }
        try {
            await applicationsRef.add({
                name: name,
                paid: false,
                timestamp: firebase.firestore.FieldValue.serverTimestamp()
            });
            showToast('식수 신청이 접수되었습니다. 입금 확인 후 명단에 표시됩니다.');
            nameInput.value = '';
        } catch (error) {
            console.error("신청 중 오류 발생:", error);
            alert("신청 처리 중 오류가 발생했습니다.");
        }
    });

    cancelForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = cancelNameInput.value.trim();
        if (!name) return;
        const querySnapshot = await applicationsRef.where("name", "==", name).get();
        if (querySnapshot.empty) {
            showToast('해당 이름의 신청자를 찾을 수 없습니다.', 'error');
            return;
        }
        const docToDelete = querySnapshot.docs[0];
        if (docToDelete.data().paid) {
            showToast('이미 입금이 확인되어 취소할 수 없습니다.', 'error');
            return;
        }
        await docToDelete.ref.delete();
        showToast('신청이 성공적으로 취소되었습니다.');
        cancelNameInput.value = '';
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
    const totalCountSpan = document.getElementById('total-count');
    const resetButton = document.getElementById('reset-button');
    const paidCountSpan = document.getElementById('paid-count');
    const unpaidCountSpan = document.getElementById('unpaid-count');

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
        totalCountSpan.textContent = snapshot.size;
        let paidCount = 0;
        let unpaidCount = 0;
        let index = 1;

        snapshot.forEach(doc => {
            const data = doc.data();

            if (data.paid) {
                paidCount++;
            } else {
                unpaidCount++;
            }

            const tr = document.createElement('tr');
            const date = data.timestamp ? data.timestamp.toDate() : new Date();
            
            // [수정] 날짜와 시간 사이에 줄바꿈(<br>)을 추가합니다.
            const formattedDate = `${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}<br>${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;
            
            tr.innerHTML = `
                <td data-label="순번">${index}</td>
                <td data-label="이름">${data.name}</td>
                <td data-label="신청 시간">${formattedDate}</td>
                <td data-label="입금 여부"><span class="status-${data.paid ? 'paid' : 'unpaid'}">${data.paid ? '입금 완료' : '미납'}</span></td>
                <td data-label="관리"><button class="toggle-paid-btn" data-id="${doc.id}" data-current-paid="${data.paid}">${data.paid ? '미납으로 변경' : '입금 확인'}</button></td>
            `;
            tableBody.appendChild(tr);
            index++;
        });

        paidCountSpan.textContent = paidCount;
        unpaidCountSpan.textContent = unpaidCount;


        document.querySelectorAll('.toggle-paid-btn').forEach(button => {
            button.addEventListener('click', async (e) => {
                const docId = e.target.dataset.id;
                const currentPaid = e.target.dataset.currentPaid === 'true';
                
                try {
                    await applicationsRef.doc(docId).update({ paid: !currentPaid });
                } catch (error) {
                    console.error("입금 상태 변경 실패! Firestore 보안 규칙을 확인하세요.", error);
                    alert("오류: 입금 상태를 변경할 수 없습니다.");
                }
            });
        });
    });
}
