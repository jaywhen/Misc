// import React, {useState, useEffect} from 'react';

// function App() {
//   const [error, setError] = useState(null);
//   const [isLoaded, setIsLoaded] = useState(false);
//   const [items, setItems] = useState([]);

//   useEffect(() => {
//     fetch("http://localhost:8080/college/findAll")
//       .then(res => res.json())
//       .then(
//         (result) => {
//           setIsLoaded(true);
//           setItems(result);
//         },
//         (error) => {
//           setIsLoaded(true);
//           setError(error);
//         }
//       )
//     }, []);
  
//   if(error) {
//     return <div>Error: {error.message}</div>;
//   } else if(!isLoaded) {
//     return <div>Loading ... </div>;
//   } else {
//     return(
//       <ul>
//         {items.map(item => (
//           <li key={item.collegeId}>
//             {item.nameZh}
//           </li>
//         ))}
//       </ul>
//     );
//   }
// }

// export default App
import { useState } from "react";
import LoginForm from "./components/LoginForm";
export default function App() {
  const adminDb = {
    email: "123@hc.com",
    password: "admin",
  };

  const [user, setUser] = useState({name: "", email: ""});
  const [error, setError] = useState("");

  const Login = details => {
    console.log(details);

    if(details.email == adminDb.email && details.password == adminDb.password ) {
      console.log("Logged in");
      setUser({
        name: details.name,
        email: details.email,
      });
    } else {
      setError("Not match!")
    }
  }

  const Logout = () => {
    setUser({ name: "", email: "", });
    console.log("Logout");
  }

  return (
    <div className="App">
      {(user.email != "") ? (
        <div className="welcome">
          <h2>Welcome, <span>{user.name}</span></h2>
          <button onClick={Logout}>Logout</button>
        </div>
      ) : (
        <LoginForm Login={Login} error={error}/>
      )}
    </div>
  );
}
