// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBoz3rca2kYHPT-77FAtN2WfqiM334p1rc",
  authDomain: "bloominglove3000restaurant.firebaseapp.com",
  projectId: "bloominglove3000restaurant",
  storageBucket: "bloominglove3000restaurant.firebasestorage.app",
  messagingSenderId: "1447477736",
  appId: "1:1447477736:web:8719b8c3b9d9cecdf8245d",
  measurementId: "G-QEK3D0QZF8"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);