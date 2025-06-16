// --- 1단계: Firebase 모듈 및 설정 가져오기 ---
// [핵심 수정] CDN URL에서 직접 최신 Firebase 모듈(v9)을 가져옵니다.
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js";
import { getFirestore, collection, addDoc, query, where, getDocs, onSnapshot, orderBy, serverTimestamp, deleteDoc, updateDoc, doc, writeBatch } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-firestore.js";
import { firebaseConfig } from './firebase-config.js';

console.log("✅ 1. Firebase 모듈 및 설정을 가져왔습니다.");

// --- 2단계: Firebase 초기화 ---
let app, db;
try {
    app = initializeApp(firebaseConfig);
    db = getFirestore(app);
    console.log("✅ 2. Firebase 앱이 성공적으로 초기화되었습니다.");
} catch (e) {
    console.error("❌ 2-ERROR. Firebase 초기화 중 심각한 오류 발생:", e);
    alert("Firebase 설정에 문제가 있습니다. firebase-config.js 파일을 다시 확인해주세요. F12를 눌러 콘솔의 에러 메시지를 확인하세요.");
}

// --- 공통 변수 ---
const applicationsRef = collection(db, "applications");

// --- 토스트 팝업 기능 ---
function showToast(message, type = 'success') {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        console.error("❌ 토스트 팝업 컨테이너(#toast-container)를 HTML에서 찾을 수 없습니다.");
        return;
    }
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
    console.log("✅ 3. 페이지의 HTML 로딩이 완료되었습니다.");
    if (document.getElementById('apply-form')) {
        setupUserPage();
    } else if (document.getElementById('admin-table')) {
        setupAdminPage();
    }
});

// --- 신청자용 페이지 기능 ---
function setupUserPage() {
    console.log("➡️ 4. 신청자 페이지 설정을 시작합니다.");
    const applyForm = document.getElementById('apply-form');
    const nameInput = document.getElementById('name-input');
    const applicantListDiv = document.getElementById('applicant-list');
    const cancelForm = document.getElementById('cancel-form');
    const cancelNameInput = document.getElementById('cancel-name-input');

    const q = query(applicationsRef, where("paid", "==", true), orderBy("timestamp", "desc"));
    onSnapshot(q, (snapshot) => {
        applicantListDiv.innerHTML = '';
        if (snapshot.empty) {
            applicantListDiv.innerHTML = '<p>아직 식사 확정 명단에 등록된 분이 없습니다.</p>';
        } else {
            snapshot.forEach(doc => {
                const p = document.createElement('p');
                p.textContent = doc.data().name;
                applicantListDiv.appendChild(p);
            });
        }
    });

    applyForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = nameInput.value.trim();
        if (!name) return;

        const checkQuery = query(applicationsRef, where("name", "==", name));
        const querySnapshot = await getDocs(checkQuery);
        if (!querySnapshot.empty) {
            showToast('이미 해당 이름으로 신청(또는 대기) 중입니다.', 'error');
            return;
        }

        try {
            await addDoc(applicationsRef, {
                name: name,
                paid: false,
                timestamp: serverTimestamp()
            });
            showToast('식수 신청이 접수되었습니다. 입금 확인 후 명단에 표시됩니다.');
            nameInput.value = '';
        } catch (error) {
            console.error("신청 중 오류 발생: ", error);
            showToast('오류가 발생했습니다. 다시 시도해주세요.', 'error');
        }
    });

    cancelForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = cancelNameInput.value.trim();
        if (!name) return;

        try {
            const checkQuery = query(applicationsRef, where("name", "==", name));
            const querySnapshot = await getDocs(checkQuery);
            if (querySnapshot.empty) {
                showToast('해당 이름의 신청자를 찾을 수 없습니다.', 'error');
                return;
            }

            const docToDelete = querySnapshot.docs[0];
            if (docToDelete.data().paid) {
                showToast('이미 입금이 확인되어 취소할 수 없습니다. 관리자에게 문의하세요.', 'error');
                return;
            }
            await deleteDoc(docToDelete.ref);
            showToast('신청이 성공적으로 취소되었습니다.');
            cancelNameInput.value = '';
        } catch (error) {
            console.error("취소 중 오류 발생: ", error);
            showToast('오류가 발생했습니다. 다시 시도해주세요.', 'error');
        }
    });
}

// --- 관리자용 페이지 기능 ---
function setupAdminPage() {
    console.log("➡️ 4. 관리자 페이지 설정을 시작합니다.");
    const password = prompt("관리자 비밀번호를 입력하세요:", "");
    if (password !== "samcheon1004") {
        alert("비밀번호가 틀렸습니다. 페이지 접근이 차단됩니다.");
        document.body.innerHTML = "<h1>🔒 접근 권한이 없습니다.</h1>";
        return;
    }

    const tableBody = document.getElementById('admin-table-body');
    const totalCountSpan = document.getElementById('total-count');
    const resetButton = document.getElementById('reset-button');

    resetButton.addEventListener('click', async () => {
        if (!confirm("정말로 모든 신청 내역을 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.")) return;
        if (prompt("데이터 삭제에 동의하시면 '초기화'라고 정확히 입력해주세요.") !== '초기화') {
            alert("입력이 올바르지 않아 취소되었습니다.");
            return;
        }
        try {
            const snapshot = await getDocs(applicationsRef);
            const batch = writeBatch(db);
            snapshot.docs.forEach(d => batch.delete(d.ref));
            await batch.commit();
            alert("모든 신청 내역이 성공적으로 초기화되었습니다.");
        } catch (error) {
            console.error("초기화 중 오류 발생: ", error);
            alert("초기화 중 오류가 발생했습니다.");
        }
    });

    const q = query(applicationsRef, orderBy("timestamp", "asc"));
    onSnapshot(q, (snapshot) => {
        tableBody.innerHTML = '';
        totalCountSpan.textContent = snapshot.size;
        let index = 1;

        snapshot.forEach(d => {
            const data = d.data();
            const tr = document.createElement('tr');
            const date = data.timestamp ? data.timestamp.toDate() : new Date();
            const formattedDate = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;
            
            tr.innerHTML = `
                <td>${index}</td>
                <td>${data.name}</td>
                <td>${formattedDate}</td>
                <td><span class="status-${data.paid ? 'paid' : 'unpaid'}">${data.paid ? '입금 완료' : '미납'}</span></td>
                <td><button class="toggle-paid-btn" data-id="${d.id}" data-current-paid="${data.paid}">${data.paid ? '미납으로 변경' : '입금 확인'}</button></td>
            `;
            tableBody.appendChild(tr);
            index++;
        });

        document.querySelectorAll('.toggle-paid-btn').forEach(button => {
            button.addEventListener('click', async (e) => {
                const docId = e.target.dataset.id;
                const currentPaid = e.target.dataset.currentPaid === 'true';
                try {
                    const docRef = doc(db, "applications", docId);
                    await updateDoc(docRef, { paid: !currentPaid });
                } catch (error) {
                    console.error("입금 상태 변경 중 오류 발생: ", error);
                    alert('오류가 발생했습니다.');
                }
            });
        });
    });
}
