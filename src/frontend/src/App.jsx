import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Users from "./Users";

function App() {
  return (
    <div className="container">
      <h1 className="text-center mt-5">React Front End</h1>
      <Users />
    </div>
  );
}

export default App;
