import firebase from "firebase/app";
import "firebase/auth";
import 'firebase/firestore';
import 'firebase/storage';

const firebaseConfig = {
  apiKey: "AIzaSyC9LXxmurxC1vBEvYW8PxYzwyr4WX_GST4",
  authDomain: "airdna-3d619.firebaseapp.com",
  databaseURL: "https://airdna-3d619-default-rtdb.firebaseio.com",
  projectId: "airdna-3d619",
  storageBucket: "airdna-3d619.appspot.com",
  messagingSenderId: "880565314266",
  appId: "1:880565314266:web:4e00b360a94d9ddb19fbe3",
  measurementId: "G-PGKFP31MQR"
};
// Initialize Firebase
const fire = firebase.initializeApp(firebaseConfig);
export default fire;